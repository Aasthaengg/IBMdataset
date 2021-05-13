N=int(input())
b=0
for i in range(0,26):
    for j in range(0,16):
        if 4*i+7*j==N:
            b+=1
if b!=0:
    print('Yes')
else:
    print('No')