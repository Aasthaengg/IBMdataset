# https://atcoder.jp/contests/agc009/tasks/agc009_a

n=int(input())
ab=[tuple(map(int,input().split())) for _ in range(n)]

ans=0
for a,b in reversed(ab):
    a+=ans
    res=a%b
    if res:
        ans+=b-res
print(ans)