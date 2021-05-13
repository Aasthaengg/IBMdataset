from collections import Counter

N = input()
A = list(map(int, input().split()))
counter = Counter(A)

ans = 0
for number, count in counter.items():
    if count < number:
        ans += count
    else:
        ans += count - number

print(ans)
