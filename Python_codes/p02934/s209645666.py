N = int(input())
A = list(map(float,input().split()))
ans = 0
for i in A:
    ans+=1/i
print(1/ans)