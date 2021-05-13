N,T = map(int,input().split())
A = list(map(int,input().split()))

data = [0]*(N-1)
M = [0]*N
M[N-1] = A[N-1]
M_index = [N-1]*N

for i in range(2,N+1):
    if A[N-i] > M[N-i+1]:
        M[N-i] = A[N-i]
        M_index[N-i] = N-i
    else:
        M[N-i] = M[N-i+1]
        M_index[N-i] = M_index[N-i+1]
    data[N-i] = M[N-i] - A[N-i]

m = max(data)
l = []
for i in range(N-1):
    if data[i] == m:
        l.append(i)

ans = [0]*N
for x in l:
    ans[M_index[x]] = 1

#####
#print("A",A)
#print("M",M)
#print("M_index",M_index)
#print("data",data)
#print("ans",ans)
#####

print(sum(ans))