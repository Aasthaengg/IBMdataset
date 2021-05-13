N = int(input())

s = set()
for _ in range(N):
    A = int(input())
    if A in s:
        s.remove(A)
    else:
        s.add(A)

print(len(s))
