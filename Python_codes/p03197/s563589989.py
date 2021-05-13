n = int(input())
a = [int(input()) for i in range(n)]
f = True
for i in a:
    if i%2==1:
        f = False
if f:
    print('second')
else:
    print('first')