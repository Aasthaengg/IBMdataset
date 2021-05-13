N = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
al = A[::2]
bo = A[1::2]
print(sum(al)-sum(bo))