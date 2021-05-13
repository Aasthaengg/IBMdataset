k,t = map(int,input().split())
a = list(map(int,input().split()))
last = None

if t == 1:
    print(k-1)
    exit()

for i in range(k):#　i日目(i=0,1...k-1)
    [nex,ful] = sorted(a)[-2:]
    ful_index,nex_index = a.index(ful),a.index(nex)
    if nex == 0:
        ans = k-i-1
        break
    if last == ful_index:
        last = nex_index
        a[nex_index] -= 1
    else:
        last = ful_index
        a[ful_index] -= 1
        
print(ans)