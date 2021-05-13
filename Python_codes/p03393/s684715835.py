#辞書順
#a<b,a*<b(先頭が大きいため)
#a
from itertools import permutations
S=input()
N=len(S)
alp=[0]*26
searched=[0]*26
flag=0
c=0
sub=100
minsub=100
#zxywvutsrqponmlkjihgfedcba→
for i in range(N):
    alp[ord(S[i])-97]=alp[ord(S[i])-97]+1
    #print(alp)
if (max(alp)!=1)or(S=="zyxwvutsrqponmlkjihgfedcba"):
    flag=0
else:
    if N!=26:
        for i in range(26):
            if alp[i]==0:
                c=chr(97+i)
                S="".join((S,c))
                flag=1
                break
    else:
        i=len(S)-2
        s=S[i:]
        #print(s)
        while True:
            piv=s[0]
            #print(s,S[:i],piv)
            for j in range(len(s)-1):
                if ord(s[j+1])>ord(piv):
                    sub=ord(s[j+1])-ord(piv)
                    #print(sub)
                    if sub<minsub:
                        minsub=sub
            if (minsub!=100):
                #print(minsub,chr(ord(piv)+minsub))
                S="".join((S[:i],chr(ord(piv)+minsub)))
                flag=1
                break

            minsub=100
            sub=0
            i=i-1
            s=S[i:]

if flag==0:
    print("-1")
else:
    print(S)