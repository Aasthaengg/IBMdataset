from collections import Counter
n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
cd=Counter(d)
ct=Counter(t)
#print(cd,ct)
for k,v in ct.items():
    if cd[k]<v:
        print("NO")
        exit()
print("YES")