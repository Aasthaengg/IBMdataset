s = input()
K = int(input())

ss = set()
n = len(s)
for x in range(1, K + 1):
    for i in range(n):
        ss.add(s[i : i + x])
print(sorted(ss)[K - 1])