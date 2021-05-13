n,l = map(int,input().split())
pai = []
for i in range(1,n+1):
    pai.append(l+i-1)
#print(pai)
if 0 in pai:
    print(sum(pai))
else:
    if min(pai)>0:
        print(sum(pai)-min(pai))
    else:
        print(sum(pai)-max(pai))