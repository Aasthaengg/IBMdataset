import itertools
X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
AB = [a+b for a,b in itertools.product(A,B)]
AB.sort(reverse=True)
AB = AB[:K]
ABC = [ab + c for ab,c in itertools.product(AB,C)]
ABC.sort(reverse=True)
for i in range(K):
    print(ABC[i])