x = int(input())
count = x//11
if x%11 == 0:
    print(count*2)
elif count*11+6 >= x:
    print(count*2+1)
else:
    print(count*2+2)