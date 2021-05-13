ABC=list(map(int,input().split()))
K=int(input())
ABC.sort()
ABC[2]*=2**K
print(sum(ABC))
