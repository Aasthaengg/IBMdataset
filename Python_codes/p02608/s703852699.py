n= int(input())
ans= [0]*10001

for x in range(1,101):
    for y in range (1,101):
        for z in range(1,101):
            mul= x*x+y*y+z*z+x*y+y*z+z*x
            if  mul <= 10000:
                ans[mul]+=1

for i in range(1,n+1):
    print(ans[i])