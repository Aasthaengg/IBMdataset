S=input()
s=len(S)
a=''
b=''
for i in range((s-1)//2):
    a+=S[i]
for n in range((s+3)//2-1,s):
    b+=S[n]
if a==b:
    A=a[::-1]
    B=b[::-1]
    if A==a and B==b:
        print('Yes')
    else:
        print('No')
else:
    print('No')
