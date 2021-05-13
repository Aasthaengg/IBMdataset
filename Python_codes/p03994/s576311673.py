import sys

s = list(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

i = 0
while i < len(s):
    if K == 0:
        break

    # 最後の文字の場合は限界まで操作する
    if i == len(s) - 1:
        n = (ord(s[i]) - ord("a") + K) % 26
        # print(n)
        s[i] = chr(ord("a") + n)
        break

    if s[i] == "a":
        i += 1
        continue

    # それ以外の場合、aにできるなら操作する
    # aに変換するまでの操作回数
    n = 26 - (ord(s[i]) - ord("a"))
    # print(n)
    if n <= K:
        s[i] = "a"
        K -= n

    i += 1

print("".join(s))