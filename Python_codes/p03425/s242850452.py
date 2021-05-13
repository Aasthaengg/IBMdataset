import collections
N = int(input())
S = []
for i in range(N):
    st = str(input())
    S.append(st[0])
    
#print(S)

c = collections.Counter(S)
#print(c)
count = []
for i in c.items():
    if i[0] in 'MARCH':
        count.append(i[1])
#print(count)
ans = 0
for i in range(len(count)):
    for j in range(i+1,len(count)):
        for k in range(j+1,len(count)):
            #print(i,j,k)
            ans += count[i]*count[j]*count[k]
            
if len(count) != 0:
    print(ans)
else:
    print(0)
