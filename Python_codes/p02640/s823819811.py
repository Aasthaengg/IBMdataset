X,Y = map(int, input().split())
cnt = 0
for i in range(X+1):
    Y1 = 2*i+4*(X-i)
    if Y==Y1:
        cnt+=1
if cnt>=1:
    print('Yes')
else:
    print('No')