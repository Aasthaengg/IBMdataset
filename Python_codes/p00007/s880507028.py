n=int(input())
value=int(100000)
for i in range(n):
    value=value/100*105
    if value%1000>0:
        value-=value%1000
        value+=1000

print(int(value))