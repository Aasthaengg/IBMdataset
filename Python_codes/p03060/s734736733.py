N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

print(sum([a-b if a-b>0 else 0 for a,b in zip(V,C)]))