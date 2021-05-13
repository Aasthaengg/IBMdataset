#!/usr/bin/env python3
s = input()
k = int(input())
n = len(s)
ans = []
# kを減らしていく。もし、aまで戻せるならaまで進めてk をその分減らす。
for i in range(n):
    if s[i] == "a":
        ans.append("a")
    elif 123 - ord(s[i]) <= k:
        ans.append("a")
        k -= 123 - ord(s[i])
    else:
        ans.append(s[i])
# print(k)
k %= 26  # 26で割ったあまりに落とす
ans[-1] = chr((ord(ans[-1]) + k - 97) % 26 + 97)
print("".join(ans))
