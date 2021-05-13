s=input()
s_=list(s)
S=list(enumerate(s))
num=len(S)
empty=[]
for x,y in S:
    if (x%2==0 and (y=='R' or y=='U' or y=='D')) or (x%2==1 and (y=='L' or y=='U' or y=='D')):
        empty.append(y)
if empty==s_:
    print('Yes')
else:
    print('No')
