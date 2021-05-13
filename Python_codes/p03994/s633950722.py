s = list(map(str, input().rstrip()))
k = int(input())

diff = [(ord("a") + 26 - ord(x)) % 26 for x in s]

for i in range(len(s) - 1):
    if diff[i] <= k:
        s[i] = "a"
        k -= diff[i]
    else:
        continue

tmp = ord(s[-1]) + k % 26
if tmp > 122:
    tmp -= 26

s[-1] = chr(tmp)

print("".join(s))