from _collections import defaultdict
s=input()
X=defaultdict(int)
l=len(s)
for i in s:
    X[i]+=1
ANS=[]
for key in X.keys():
    a=0
    cnt=0
    for i in range(l):
        if s[i]==key:
            a=max(a,cnt)
            cnt=0
        else:
            cnt+=1
    ANS.append(max(a,l-s.rfind(key)-1))
print(min(ANS))