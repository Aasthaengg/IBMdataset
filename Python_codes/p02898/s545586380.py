N,K = (int(x) for x in input().split())
H = [int(x) for x in input().split()]
print(sum(x>=K for x in H))