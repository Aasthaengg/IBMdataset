a,b,c = map(int,input().split())
num = 0

if b != 1:
    #if a == 1:
    #    a += 1
    for i in range(a,b+1):
        if (c % i) == 0:
            num += 1
else:
    num = 1
print(num)