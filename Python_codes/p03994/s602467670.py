S = input()
K = int(input())
z = ord('z') + 1

res = ""
flg = False
for i,c in enumerate(S):
    if c == 'a':
        res += 'a'
        continue
    elif z - ord(c) <= K:
        res += 'a'
        K -= z-ord(c)
    else:
        res += chr(ord(c))

res = res[:-1] + chr((ord(res[-1])-ord('a') + K) % 26 + ord('a'))
print(res)