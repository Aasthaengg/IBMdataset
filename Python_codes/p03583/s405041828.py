N = int(input())
flag = 0
for h in range(1,3501):
    for w in range(1,3501):
        if 4*h*w-N*w-N*h>0 and (N*h*w)%(4*h*w-N*w-N*h)==0:
            x = h
            y = w
            z = (N*h*w)//(4*h*w-N*w-N*h)
            flag = 1
            break
    if flag==1:break
print(x,y,z)