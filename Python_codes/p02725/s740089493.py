K,N = map(int,input().split())
A = list(map(int,input().split()))
ls = []
for i in range(N):
    #print(i)
    if i != N-1:
        ls.append(A[i+1]-A[i])
    else:
        ls.append(A[0]+K-A[i])
#print(ls)
    #print(ls)
print(sum(ls)-max(ls))
