from collections import Counter


N=int(input())
A=list(map(int,input().split()))
c = Counter(A)
s = 0
for k, v in c.items():
    s += v-1
if s % 2 == 0:
    print(len(set(A)))
else:
    print(len(set(A))-1)