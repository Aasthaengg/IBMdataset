k,x = map(int,input().split())
result = [i for i in range(x-k+1,x+k)]
for j in result:
    print(j,end=' ')