K, T = map(int, input().split())
A = [int(i) for i in input().split()]

print(2*max(A)-K-1 if 2*max(A)-K>0 else 0)