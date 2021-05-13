N=int(input())
A=list(map(int, input().split()))
ans=0
max=0
for i in A:
    if i < max:
        ans += max - i
    else:
        max = i
print(ans)