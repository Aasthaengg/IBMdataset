n = int(input())
a = list(map(int, input().split()))
di = {}
for i in a:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
k = list(di.keys())
v = list(di.values())
if n%3!=0 and len(di)>1:
    print('No')
elif len(di)==3 and v[0]==v[1]==v[2] and k[0]^k[1]^k[2]==0:
    print('Yes')
elif len(di)==2 and ((v[0]<v[1] and v[0]==n//3 and k[0]==0) or (v[0]>v[1] and v[1]==n//3 and k[1]==0)):
    print('Yes')
elif len(di)==1 and k[0]==0:
    print('Yes')
else:
    print('No')