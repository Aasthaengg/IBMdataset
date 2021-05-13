n=eval(input())
taro=[]
hanako=[]
for i in range(n):
    x,y=input().split()
    taro.append(x)
    hanako.append(y)
T=0
H=0
for i in range(n):
    if taro[i]<hanako[i]:
        H=H+3
    elif taro[i]>hanako[i]:
        T=T+3
    else:
        H=H+1
        T=T+1
print(T,H)