

n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
a = [[-1,-1] for i in range(n)]
b = [[-1,-1] for i in range(n)]

nowa = 0
nowb = 0
for i in range(n):
    if(aa[i]>nowa):
        a[i] = [aa[i],aa[i]]
        nowa = aa[i]
    else:
        a[i] = [1,aa[i]]
    if(bb[n-1-i]>nowb):
        b[n-1-i] = [bb[n-1-i],bb[n-1-i]]
        nowb = bb[n-1-i]
    else:
        b[n-1-i] = [1,nowb]
#print(a)
#print(b)
for i in range(n):
    a[i][0] = max(a[i][0],b[i][0])
    a[i][1] = min(a[i][1],b[i][1])
    
ans = 1
for i in range(n):
    ans *= max(0, a[i][1]-a[i][0]+1)
    ans%= 1000000007
print(ans)