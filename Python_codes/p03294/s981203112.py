n = list(map(int, input()))[0]
a = list(map(int, input().split()))

ans=0
for j in a:
    ans+=(j-1)
print(ans)