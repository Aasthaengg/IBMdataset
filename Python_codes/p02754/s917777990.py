N,A,B=map(int,input().split())
c=10**100
if N<c:
    if N%(A+B)<=A:
        print((N//(A+B))*A+(N%(A+B)))
    elif N%(A+B)>A:
        print((N//(A+B))*A+A)
elif N>=c:
    if c%(A+B)<=A:
        print((c//(A+B))*A+(c%(A+B)))
    elif c%(A+B)<=A:
        print((c//(A+B))*A+A)