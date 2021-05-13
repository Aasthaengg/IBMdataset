from sys import exit

N = int(input())
A = list(int(x) for x in input().split())

break_count = 0

for key, a in enumerate(A, 1):
    if not a == key - break_count:
        break_count += 1

if break_count == N:
    print(-1)

else:
    print(break_count)
