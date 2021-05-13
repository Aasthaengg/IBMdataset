from collections import Counter
n, k, q = map(int, input().split())
a = list(int(input()) for _ in range(q))
mycounter = Counter(a)
for i in range(n):
    ans = "Yes" if q - mycounter[i+1] < k else "No"
    print(ans)
