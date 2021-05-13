a,b=map(int,input().split())

cnt=abs(abs(a)-abs(b))
if a<0 and b<0:
    if abs(a)<abs(b):
        cnt+=2
    #elif a<b
    #a<bの時は符号変換不要
if a>0 and b>0:
    if a>b:
        cnt+=2
    #elif a<b
    #符号変換不要

if a<0 and b>0:
    cnt+=1
if a>=0 and b<=0 and a!=b:
    cnt+=1

print(cnt)