a,b = input().split()
x = int(a+b)
flag = False
for i in range (1000):
    if x == i*i:
        flag = True
        break
if flag:
    print('Yes')
else:
    print('No')