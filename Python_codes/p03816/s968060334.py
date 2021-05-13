n = int(input())
A = list(map(int, input().split()))

A_set = set(A)

if (len(A) - len(A_set)) % 2 == 0:
    ans = len(A_set)
else:
    ans = len(A_set) - 1

print(ans)