import sys
input = sys.stdin.readline

O = list(input().rstrip('\n'))
E = list(input().rstrip('\n'))
n = len(O) + len(E)
A = []

for i in range(n):
    if i % 2 == 0:
        A.append(O[i//2])
    else:
        A.append(E[i//2])
ans = "".join(A)
print(ans)
