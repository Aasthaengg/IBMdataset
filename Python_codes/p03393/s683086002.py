S=input()
l=len(S)

if l <=25:
    for i in range(26):
        ch=chr(ord('a')+i)
        if ch not in S:
            S+=ch
            break
elif S=='zyxwvutsrqponmlkjihgfedcba':
    S=-1
else:
    index=24
    tmp=[ord(S[25])]
    while ord(S[index]) > ord(S[index+1]):
        tmp.append(ord(S[index]))
        index -= 1

    re=max(tmp)
    for ch in tmp:
        if ch < re and ch > ord(S[index]) :
            re = ch
    S=S[:index]+chr(re)

print(S)