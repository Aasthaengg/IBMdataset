x = int(input())

rest = x

for i in range(1,x+1):
    if i < rest:
        rest -= i
    else:
        print(i)
        break