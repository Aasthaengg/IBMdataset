x = int(input())

n = x//11 
m = x % 11

if m >6:
    mm = 2

elif m == 0:
    mm = 0
else:
    mm =1

print(n*2+mm)