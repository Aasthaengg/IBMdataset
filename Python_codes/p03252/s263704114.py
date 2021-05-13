s = input()
t = input()
n = len(s)

alphabet = [chr(i) for i in range(97, 97+26)]
dict_alphabet = {}
for i, alphabet in enumerate(alphabet):
    dict_alphabet[alphabet] = i

ans = 'Yes'
# 同じsに同じtが対応しているか
alphabet_s2t = [0] * 26
for i in range(n):
    if not alphabet_s2t[dict_alphabet[s[i]]]:
        alphabet_s2t[dict_alphabet[s[i]]] = t[i]
    else:
        if alphabet_s2t[dict_alphabet[s[i]]] != t[i]:
            ans = 'No'

alphabet_t2s = [0] * 26
for i in range(n):
    if not alphabet_t2s[dict_alphabet[t[i]]]:
        alphabet_t2s[dict_alphabet[t[i]]] = s[i]
    else:
        if alphabet_t2s[dict_alphabet[t[i]]] != s[i]:
            ans = 'No'
print(ans)


    
