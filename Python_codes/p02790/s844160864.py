a,b = input().split()
if a > b:
    tmp = a
    a = b
    b = tmp
for i in range(int(b)):
    print(a,end='')
