a,b,c=map(int, input().split())
count=0

if c>=b:
    count+=2*b
    c=c-b
    if c>a:
        count+=a
        c=c-a
        if c>0:
            count+=1
    else:
        count+=c
else:
    count+=c+b

print(count)