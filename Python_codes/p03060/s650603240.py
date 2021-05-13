N = input()
V = [int(X) for X in input().split()]
C = [int(X) for X in input().split()]
print(sum(X-Y if X-Y>0 else 0 for X,Y in zip(V,C)))