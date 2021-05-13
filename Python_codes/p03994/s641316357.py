s = list(input())
n = len(s)
k = int(input())
alphabet = [chr(i) for i in range(97, 97+26)]
al_d = {}
for i in range(26):
    al_d[alphabet[i]] = i
for i in range(n):
    tobe_a = 26 - al_d[s[i]]
    if tobe_a <= k:
        tobe_a %= 26
        k -= tobe_a
        s[i] = 'a'
remain = k % 26
s[-1] = alphabet[al_d[s[-1]]+remain]
print(''.join(s))
# あー！最後にするんじゃなくてaでまとめられる場所があるならそうした方がいい？
# ただそれがあるならそれより前にaにしてるはず