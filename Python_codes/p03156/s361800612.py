N = int(input())
A, B = map(int, input().split())
*P, = map(int, input().split())

first = []
second = []
third = []
for p in P:
    if p in range(A+1):
        first.append(p)
    elif p in range(A+1, B+1):
        second.append(p)
    else:
        third.append(p)
print(min(len(first), len(second), len(third)))