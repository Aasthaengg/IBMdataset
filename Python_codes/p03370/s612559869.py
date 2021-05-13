n,x = map(int,input().split())
do_min = 1000
for i in range(n):
    dum = int(input())
    x -= dum
    do_min = min(do_min,dum)
print(n + x//do_min)