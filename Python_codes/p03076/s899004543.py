*A, = map(int, open(0).read().split())
B = [(10-a%10)%10 for a in A]
print(sum(A) + sum(B) - max(B))