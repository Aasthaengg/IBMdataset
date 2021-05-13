s = input()
k = int(input())

ss = set()
for i in range(len(s)):
    for j in range(i+1, min(i+6, len(s)+1)):
        ss.add(s[i:j])

for i, s in enumerate(sorted(ss), start=1):
    if i == k:
        print(s)
        break
