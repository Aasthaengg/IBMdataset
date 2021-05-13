from collections import Counter
N = int(input())
A = Counter(map(int, input().split()))
ans = 0
for i,j in A.items():
    if i < j:
        ans += j - i
    elif i >j:
        ans += j
print(ans)