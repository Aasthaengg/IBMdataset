N,M=map(int,input().split())
num=0
value=0
i=1
T=1
odds=(1/2)**M
time=(N-M)*100+1900*M
while 1:

    value+=time*i*(T*odds)
    T*=(1-odds)
    if num==value:
        break
    num=value
    i+=1
print(round(value))
