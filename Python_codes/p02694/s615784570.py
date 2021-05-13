X=int(input())
num=100
d=1.01
cnt=0
while num<X:
    num+=num//100
    cnt+=1
print(cnt)