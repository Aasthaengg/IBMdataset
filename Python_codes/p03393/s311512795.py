import string
ABC=list(string.ascii_lowercase)
s=input()
S=list(s[::-1])

if s=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)
else:
    if len(s)==26:
        for i in range(len(s)):
            n=ABC.index(S[i])
            if not set(ABC[n+1:])<=set(S[i+1:]):
                j=i
                break
        L=list(set(ABC[n+1:])-set(S[j+1:]))
        L.sort()
        sgyku=L[0:1]+S[j+1:]
        print("".join(sgyku[::-1]))
    else:
        L=list(set(ABC)-set(s))
        L.sort()
        print(s+L[0])