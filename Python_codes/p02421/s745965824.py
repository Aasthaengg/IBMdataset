a=b=0
for i in range(int(input())):
    y,z=input().split()
    if y>z:a+=3
    elif y<z:b+=3
    else:a+=1;b+=1
print(a,b)