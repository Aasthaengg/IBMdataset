from statistics import median
N = int(input())
A = list(map(int, input().split()))
B = [a-i for i, a in enumerate(A)]
m = int(median(B))
print(sum(abs(b-m) for b in B))