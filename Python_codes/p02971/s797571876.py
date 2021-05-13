n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = sorted(a)
for j,k in enumerate(a):
    print(s[-2]) if k == s[-1] else print(s[-1])