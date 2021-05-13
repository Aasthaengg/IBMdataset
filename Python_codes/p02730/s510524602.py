S = input()
l = len(S)
T = ''.join(list(reversed(S)))

a = S[:(l-1)//2]
a1 = ''.join(list(reversed(a)))

b = S[(l+3)//2-1:l]
b1 = ''.join(list(reversed(b)))

if S == T:
    if a == a1 and b == b1:
        print('Yes')
    if a != a1 or b != b1:
        print('No')
if S != T:
    print('No')