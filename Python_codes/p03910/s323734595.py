n = int(input())
num = 0
for k in range(1,n+1):
    #print(k)
    if k*(k+1) >=2*n:
        break
if k*(k+1) == 2*n:
    for i in range(k):
        print(i+1)
else:
    num = k*(k+1)//2-n
    #print(num,k*(k+1)//2)
    for i in range(k):
        if i+1 == num:
            continue
        else:
            print(i+1)