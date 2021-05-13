from collections import defaultdict
n = int(input())
a = [int(i) for i in input().split()]
d = defaultdict(int)
for i in a:
    d[i] += 1
print("Yes"
if(
    (len(d) == 3 and len(set(d.values())) == 1 and n % 3 == 0 and (list(d.keys())[0] ^ list(d.keys())[1] ^ list(d.keys())[2] == 0))
    or (len(d) == 2 and n % 3 == 0 and d[0] == n // 3 and (0 in d.keys()))
    or (sum(a) == 0)
)
else "No")
