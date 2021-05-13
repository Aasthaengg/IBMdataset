s = [ord(i) for i in input()]
k = int(input())
for i in range(len(s)):
    if s[i] == 97: continue
    if 123 - s[i] <= k:
        k -= 123 - s[i]
        s[i] = 97
        if k == 0:
            break
if k != 0:
    s[-1] = s[-1] + k % 26
print("".join([chr(i) for i in s]))