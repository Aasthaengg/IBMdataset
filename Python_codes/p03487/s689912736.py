from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))
cnt = 0

for key, value in A.items():
    if key < value:
        cnt += value - key
    elif key > value:
        cnt += value
    else:
        continue

print(cnt)
