n=int(input())
taro=0
hanako=0
for i in range(n):
    a,b=map(str,input().split())
    if a>b:
        taro+=3
    elif a<b:
        hanako+=3
    else:
        taro+=1
        hanako+=1
        
print(taro,hanako)
