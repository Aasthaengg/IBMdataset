S = list(input())
S.reverse()
S = ''.join(S)
st = ['maerd','remaerd','esare','resare']
ans = 'YES'
while S != '':
    if S[0:5] in st:
        S = S[5:]
    elif S[0:6] in st:
        S = S[6:]
    elif S[0:7] in st:
        S = S[7:]
    else:
        ans = 'NO'
        break
print(ans)