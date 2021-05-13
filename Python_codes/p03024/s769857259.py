# MERGE IT


'''n=int(input())
for i in range(0,n):
    o=int(input())
    p=input().rstrip().split(' ')
    l=[0]*3;
    for j in range(0,len(p)):
        l[(int(p[j])%3)]+=1;
    s=0;
    s+=l[0];
    s+=min(l[1],l[2])
    if min(l[1],l[2])==l[2]:
        l[1]-=l[2]
        s+=(l[1]//3)
    elif min(l[1],l[2])==l[1]:
        l[2]-=l[1]
        s+=(l[2]//3)
    print(s)'''

# LOSE IT

s=input().rstrip()
x=list(s)
T=0;
for i in range(0,len(x)):
    if x[i]=='o':
        T+=1;
T+=(15-len(x))
if T>=8:
    print("YES")
else:
    print("NO")
