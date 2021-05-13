from collections import Counter


n = int(input())
s = input()
count = Counter(s)

ans = count["R"] * count["G"] * count["B"]
for i in range(n):
    for j in range(i+1, n):
        k = 2*j - i
        if k > n - 1:
            break
        if s[i] != s[j] != s[k] != s[i]:
            ans -= 1

print(ans)