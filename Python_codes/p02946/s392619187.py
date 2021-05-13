k,x = map(int,input().split())
for i in range(max(-1000000,x-k+1),min(x+k,1000001)):
    print(i)