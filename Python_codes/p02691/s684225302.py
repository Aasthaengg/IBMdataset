from collections import defaultdict
N = int(input())
A = map(int,input().split())

s = defaultdict(lambda :0)
b = defaultdict(lambda :0)
for i,a in enumerate(A):
    s[i-a] = s[i-a] + 1
    b[i+a] = b[i+a] + 1

c = 0
for k in s:
    if k in b:
        c += b[k]*s[k]

print(c)