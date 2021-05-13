from collections import defaultdict

a = input()
len_a = len(a)
ans = 1 + len_a*(len_a-1)//2

d = defaultdict(int)
for ai in a:
    d[ai] += 1

for key,val in d.items():
    ans -= val*(val-1)//2

print(ans)