N = int(input())
A = list(map(int, input().split()))

ans = []
for a in A:
    ans.append(1/a)
    
ans = sum(ans)
print(1/ans)