n = list(map(int,input().split()))
dummy = set(n)
print(sum(dummy)-(sum(n)-sum(dummy)))