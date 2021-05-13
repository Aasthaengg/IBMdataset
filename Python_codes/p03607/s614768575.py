n = int(input())
A = [int(input()) for _ in range(n)]
S = set()
for a in A:
    if a in S:
        S.remove(a)
    else:
        S.add(a)
print(len(S))
