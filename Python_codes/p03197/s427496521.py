N = int(input())
a = [int(input())for _ in range(N)]
flag = False
for i in a:
    if(i%2==1):
        flag = True
        break
if(flag):
    print('first')
else:
    print('second')
