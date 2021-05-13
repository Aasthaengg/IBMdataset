def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, T = MI()
ct = []

for _ in range(N):
    c, t = MI()
    ct.append([c, t])
    
ct.sort(key = lambda x : x[0])
flg = False
ans = 0

for i in range(N):
    if ct[i][1] <= T:
        ans = ct[i][0]
        flg = True
        break
        
print(ans if flg else "TLE")