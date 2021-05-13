a,b=map(int,input().split())
if abs(a-b)%2==0:
    k=max(a,b)-abs(a-b)//2
    print(k)
    #print(abs(a-k)==abs(b-k))
else:
    print('IMPOSSIBLE')