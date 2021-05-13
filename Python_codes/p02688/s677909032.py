list_K = []
N,K = map(int,input().split())
for i in range(K):
    d = int(input())
    A = [int(j) for j in input().split()]
    for k in range(d):
        list_K.append(A[k])
list_K0 = list(set(list_K))
list_K0.sort()
list_N = list(range(1,N+1))
set_NK = set(list_N)-set(list_K0)
print(len(set_NK))