n = int(input())
As  = list(map(int, input().split()))

if n == 0:
    if As[0] == 1: print(1)
    else: print(-1)
    exit()
    
# 下から見る
As_r = As[::-1]
p = As_r[0]
# とりうる最大値
a_pre = p
qs = [p]
# とりうる最小値
mn = As_r[0]

# 深さ n-1から0まで
# 最後の葉の数がA_N < 10**8、N<=10**5より、10**(8+5)以上の葉は生まれない。
# なので、高々50回くらいの2冪で上等
for i,a in enumerate(As_r[1:]):
    d = min(n - i - 1, 50)
    p = min(2**d, p + a)
    mn = (mn+1)//2 + a
    a_pre = a
    qs.append(p)

if mn != 1:
    print(-1)
    exit()

qs.reverse()
# print(qs,As)
ans = qs[0]
cnt = qs[0]
# 上から見る
for i in range(1,n+1):
    qs[i] = min(qs[i-1]*2, 2*(qs[i-1]-As[i-1]),qs[i])
print(sum(qs))