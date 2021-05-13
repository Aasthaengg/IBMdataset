ans = 10**10
n,time = map(int,input().split())
for i in range(n):
    c,t = map(int,input().split())
    if t<=time and c<ans:
        ans = c
print('TLE' if ans==10**10 else ans)