N = int(input())
A = list(int(input()) for _ in range(N))
s = set()
for i in A:
    if i not in s:
        s.add(i)
    else:
        s.remove(i)
print(len(s))