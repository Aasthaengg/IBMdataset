s = input()
K = int(input())

ans = []
for ch in s:
    v = ord("a") + 26 - ord(ch)
    if ch != "a" and v <= K:
        K -= v
        ans.append("a")
    else:
        ans.append(ch)

if K > 0:
    ans[-1] = chr(ord(ans[-1]) + K % 26)
print("".join(ans))
