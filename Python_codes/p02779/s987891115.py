from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

for c in cnt.values():
    if c > 1:
        print("NO")
        exit()

print("YES")