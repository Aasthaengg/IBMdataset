N,A,B=map(int,input().split())
a=N//(A+B)
if N%(A+B)==0:
    print(a*A)
elif N%(A+B)>A:
    print((a+1)*A)
elif N%(A+B)<=A:
    print(a*A+(N%(A+B)))
