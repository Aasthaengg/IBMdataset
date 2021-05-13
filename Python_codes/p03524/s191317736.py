from collections import defaultdict
s = input()
cnt = defaultdict(int)
for i in range(len(s)):
    cnt[s[i]] += 1
mean = len(s) // 3
for t in ["a", "b", "c"]:
    if cnt[t] != mean and cnt[t] != mean + 1:
        print("NO")
        exit()

print("YES")