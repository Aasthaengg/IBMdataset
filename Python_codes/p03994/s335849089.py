s = input()
k = int(input())

asc = [0] * len(s)
for i in range(len(s)):
    asc[i] = ord(s[i]) - ord("a")
i = 0
for i in range(len(s)):
    if 26 - asc[i] <= k and asc[i] != 0:
        x = 26 - asc[i]
        asc[i] = 0
        k -= x
if k > 0:
    asc[-1] += k % 26
for i in range(len(s)):
    asc[i] += ord("a")
    asc[i] = chr(asc[i])
print("".join(asc))