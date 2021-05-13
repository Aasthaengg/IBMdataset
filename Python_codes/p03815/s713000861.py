x = int(input())

mod = x%11
shou = x//11

if mod == 0:
    print(shou*2)
elif mod > 0 and 6 >= mod:
    print(shou*2+1)
else:
    print(shou*2+2)