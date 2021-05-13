S = input()
K = int(input())

ord_a = ord('a')
ord_z = ord('z')

k = K
Ans = list(S)
for i, s in enumerate(S[:-1]):
    ord_s = ord(s)
    dif = ord_z - ord_s + 1
#    print(i, k, dif)
    if s == 'a':
        Ans[i] = 'a'
    elif dif <= k:
        Ans[i] = 'a'
        k -= dif
    else:
        pass
Ans[-1] = chr(ord_a + (ord(Ans[-1]) + k - ord_a)%26)
print(''.join(Ans))