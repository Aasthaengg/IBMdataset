N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

Q1 = len([x for x in P if x <= A])
Q2 = len([x for x in P if A+1 <= x <= B])
Q3 = len([x for x in P if x >= B+1])

print(min(Q1, Q2, Q3))
