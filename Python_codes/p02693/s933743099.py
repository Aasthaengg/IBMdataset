n=int(input())
x,y=map(int,input().split())
for i in range(x,y+1):
    if(i%n==0):
        print('OK')
        exit()
print('NG')