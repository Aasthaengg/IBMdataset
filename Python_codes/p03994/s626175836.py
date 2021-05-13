S=input()
K=int(input())

i=0
l=''
while i<len(S)-1:
    if S[i]=='a':
        l+='a'
    elif 123-ord(S[i])<=K:
        l+='a'
        K-=123-ord(S[i])
    else:
        l+=S[i]
    i+=1

if K>0:
    K%=26
    n=ord(S[-1])+K
    if n>122:
        n-=26
    l+=chr(n)
else:
    l+=S[-1]


print(l)