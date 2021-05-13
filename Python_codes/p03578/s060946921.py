from collections import Counter

n = int(input())
d = Counter(list(map(int, input().split())))
m = int(input())
t = Counter(list(map(int, input().split())))

for a, b in t.items():
    if d[a] < b:
        print("NO")
        exit()
print("YES")