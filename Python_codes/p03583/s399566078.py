N = int(input())
flag = 0
for h in range(1,3500):
    for n in range(1,3500):
        a = 4*h*n-N*(h+n)
        if a>0 and (N*h*n)%a==0:
            w = (N*h*n)//a
            flag = 1
            break
    if flag==1:break
if flag==1:
    print(h,n,w)
else:
    print()