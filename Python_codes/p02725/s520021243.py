K,N = map(int, input().split())
A = sorted(list(map(int, input().split())))
ans=[]
for i in range(N-1):
    ans.append(A[i+1]-A[i])
ans.append(K-max(A)+min(A))
print(sum(ans)-max(ans))