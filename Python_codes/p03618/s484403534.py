s = input()
ls = len(s)
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = [0 for i in range(26)]

ans = 1
for i, v in enumerate(s,1):
    a = alphabet.index(v)
    ans += (i - 1)  - alphabet_list[a]
    alphabet_list[a] += 1
print(ans)
