N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
P1 = [p for p in P if p <= A]
P2 = [p for p in P if A < p <= B]
P3 = [p for p in P if B < p]
print(min(len(P1), len(P2), len(P3)))