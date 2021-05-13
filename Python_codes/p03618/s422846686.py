from collections import Counter
s = str(input())
n = len(s)
ans = 1 + n * (n-1) // 2
for k, v in Counter([x for x in s]).items():
    ans -= v * (v-1) // 2
print(ans)