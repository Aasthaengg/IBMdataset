n,k,s=map(int, input().split())
lis = [s]*k
if s==10**9:
    for i in range(n-k):
        lis.append(1)
else:
    for i in range(n-k):
        lis.append(s+1)
print(*lis)
