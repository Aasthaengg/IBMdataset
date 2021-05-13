S=input()
K=int(input())

i=1
count1=0
while i<len(S):
    if S[i]==S[i-1]:
        count1+=1
        i+=1
    i+=1

ss=S*2
i=1
count2=0
while i<len(ss):
    if ss[i]==ss[i-1]:
        count2+=1
        i+=1
    i+=1

if 2*count1+1==count2 and len(set(S))!=1:
    print(K*count1+(K-1))
else:
    print(K*count2//2)