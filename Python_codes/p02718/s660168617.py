n,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse=True)
for i in range(m) :
    if l[i] < sum(l)/(4*m) :
        print('No')
        exit()
    else :
        continue
print('Yes')