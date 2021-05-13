a=int(input())
b=int(input())
c=int(input())
x=int(input())

cnt=0

for i in range(a+1):
    ayen=i*500
    if ayen<=x:
        for j in range(b+1):
            byen=j*100
            if ayen+byen<=x:
                extra=x-ayen-byen
                if extra<=c*50:
                    cnt+=1

print(cnt)