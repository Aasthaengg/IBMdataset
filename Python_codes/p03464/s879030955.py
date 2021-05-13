K=int(input())
A=list(map(int,input().split()))

n_min=2
n_max=2
for i in range(K-1,-1,-1):
    if (n_max//A[i])*A[i] < n_min or (n_min//A[i]+(1 if n_min%A[i]!=0 else 0))*A[i] > n_max:
        print(-1)
        exit()
    n_min=(n_min//A[i]+(1 if n_min%A[i]!=0 else 0))*A[i]
    n_max=(n_max//A[i])*A[i]+A[i]-1

print(n_min,n_max)