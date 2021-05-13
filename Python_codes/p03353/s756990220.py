s = input()
K = int(input())

words = []

for i in range(len(s)):
    words.append(s[i:])

words.sort()

ans = set()

for word in words:
    for i in range(len(word)):
        ans.add(word[:i+1])
    if len(ans) >= 5:break
lst = list(ans)
lst.sort()

print(lst[K-1])