N=int(input())
K=len(set(list(map(int,input().split()))))
if K%2==0: print(K-1)
else: print(K)