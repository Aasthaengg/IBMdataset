N = int(input())
D = []
ans = 0
for i in range(N):
    a, b = map(int,input().split(' '))
    D.append((a+b,a,b))
D = sorted(D, reverse=True)
for n,i in enumerate(D):
    if n%2 == 0:
        ans += i[1]
    else:
        ans -= i[2]
print(ans)