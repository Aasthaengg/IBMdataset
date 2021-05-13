N = int(input())
d = 0
s = []
for i in range(N):
    d = int(input())
    if not(d in s):
        s.append(d)
print(len(s))
