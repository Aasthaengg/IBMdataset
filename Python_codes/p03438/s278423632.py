N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print('YNeos'[sum(B)-sum(A)<sum(max(0,(b-a+1)//2)for a,b in zip(A,B))::2])