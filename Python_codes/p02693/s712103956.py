K =int(input())
A,B =map(int,input().split())
count =0
for i in range(A,B+1):
    if i%K==0:
        print('OK')
        count =1
        break
if count ==0:   
    print('NG')