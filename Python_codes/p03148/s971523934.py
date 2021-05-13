import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,K = MI()
dt = []
for i in range(N):
    t,d = MI()
    dt.append((d,t))

dt.sort(reverse=True)

basic_point = 0
ans = 0
used = set()
neta = [10**10]*(N+1)  # neta[t] = ネタtのある、最も左の位置
for i in range(K):
    d,t = dt[i]
    used.add(t)
    basic_point += d
    neta[t] = min(neta[t],i)
shurui = len(used)  # ネタの種類数
ans = basic_point + shurui**2

a,b = K-1,K
while a >= 0 and b < N:
    d1,t1 = dt[a]
    if neta[t1] != a:
        basic_point -= d1
        while b < N:
            d2,t2 = dt[b]
            if not t2 in used:
                used.add(t2)
                basic_point += d2
                shurui += 1
                ans = max(ans,basic_point + shurui**2)
                b += 1
                break
            else:
                b += 1
    a -= 1

print(ans)
