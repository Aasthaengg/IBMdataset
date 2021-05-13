k=int(input())
a,b=map(int,input().split())
i=0
while True:
    if k*i<a:
        i+=1
    if a<= k*i <=b:
        print('OK')
        break
    if b<k*i:
        print('NG')
        break
