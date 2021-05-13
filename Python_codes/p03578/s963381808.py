from collections import Counter
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
d, t = Counter(d), Counter(t)
for i in set(t):
    if d[i] < t[i]:
        print("NO")
        exit()
print("YES")