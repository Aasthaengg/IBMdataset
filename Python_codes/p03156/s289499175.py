N = int(input())
A, B = tuple(map(int, input().split()))
P = list(map(int, input().split()))
first = [p for p in P if p <= A]
second = [p for p in P if A + 1 <= p <= B]
third = [p for p in P if B + 1 <= p]
print(min(len(first), len(second), len(third)))