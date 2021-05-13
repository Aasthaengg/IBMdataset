from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a_counter = Counter(a)
k = list(a_counter.keys())
v = list(a_counter.values())

if len(a_counter) == 3 and k[0]^k[1]^k[2] == 0 and v[0] == v[1] == v[2]:
    print("Yes")
elif len(a_counter) == 2 and 0 in k and (v[0] == v[1]*2 or v[1] == v[0]*2):
    print("Yes")
elif len(a_counter) == 1 and 0 in k:
    print("Yes")
else:
    print("No")