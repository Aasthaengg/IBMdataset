x = int(input())
i = 1
while(1):
    if (x*i)%360 == 0:
        break 
    i += 1
print(i)