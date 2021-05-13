original_s = list(input())
s = list(map(lambda x:ord(x)-97-26, original_s))
K = int(input())

ans = original_s
for i in range(len(s)):
    if abs(s[i]) <= K and s[i] != -26:
        ans[i] = "a"
        K += s[i]

ans[-1] = chr(((ord(ans[-1]) + K) - 97) % 26 + 97)

print("".join(ans))