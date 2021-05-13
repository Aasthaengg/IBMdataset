n,m = map(int,input().split())
min_card,max_card = 0,n
for i in range(m):
    l,r = map(int,input().split())
    min_card = max(min_card,l)
    max_card = min(max_card,r)
#print(min_card,max_card)
if min_card<=max_card:
    print(max_card-min_card+1)
else:
    print(0)