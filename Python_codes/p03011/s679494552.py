A = [int(x) for x in input().split()]
m = max(A)
A.remove(m)
print(sum(A))