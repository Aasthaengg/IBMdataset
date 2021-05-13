x=int(input())
num=0
y=100
while y<=x:
    y+=y//100
    num+=1
    if y>=x:
        print(num)
        break
