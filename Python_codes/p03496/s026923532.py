#正の最大か負の最大を2回足す
##ay[に]ax[を]足す
n = int(input())
a = list(map(int, input().split( )))

mx = max(a)

manu = []
mn = min(a)

#print(mx, mn)
if abs(mx)>abs(mn):
    for i in range(n-1):
        if a[i]>a[i+1]:
            mx = max(a)
            mx_id = a.index(mx)
            manu.append((i+1,mx_id))
            a[i+1] += mx
            
            mx = max(a)
            mx_id = a.index(mx)
            manu.append((i+1,mx_id))
            a[i+1] += mx###
else:
    #print("hit")
    for i in range(n-1,0,-1):
        if a[i-1]>a[i]:
            mn = min(a)
            mn_id = a.index(mn)
            manu.append((i-1,mn_id))
            a[i-1] += mn
            
            mn = min(a)
            mn_id = a.index(mn)
            manu.append((i-1,mn_id))
            a[i-1] += mn
print(len(manu))
for i,j in manu:
    print(j+1,i+1)###
"""
print(*a)

for i in range(n-1):
    if a[i]>a[i+1]:
        print("false")
        exit()
print("true")
"""