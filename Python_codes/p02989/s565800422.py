N=int(input())
D=list(map(int,input().split()))
D.sort()

n_1=int(N/2)-1
n_2=int(N/2)
print(D[n_2]-D[n_1])