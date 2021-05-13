s=list(input())
s=s[:-2]
while s:
    n=len(s)//2
    p=s[:n]
    q=s[n:]
    if p==q:
        print(2*n)
        break
    else:
        s=s[:-2]