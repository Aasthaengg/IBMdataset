n = int(input())

L = list(map(int,input().split()))

L = sorted(L,reverse=True)
#print(L)
#print(sum(L)) 
if sum(L)-L[0]*2>0:
    print('Yes')
else:
    print('No')