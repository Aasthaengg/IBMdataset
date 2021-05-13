from collections import Counter

n = int(input())

lis = list(map(int, input().split()))

a = Counter(lis)

slis = sorted(set(lis))

t1 = 0
t2 = 0

for k, v in a.items():
    if v >=2 and k > t1:
        t2 = t1
        t1 = k

if a[t1] >= 4:
    print(t1*t1)
    exit()

print(t1*t2)

