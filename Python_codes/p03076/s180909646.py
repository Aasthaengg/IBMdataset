import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
nn = [a, b, c, d, e]
s = False
for i in nn:
    if s == False and i%10 != 0:
        chk = i%10
        last = i
        s = True
    elif s == False and i%10 == 0:
        pass
    elif s == True and i%10 != 0:
        if chk > i%10:
            chk = i%10
            last = i
if s == False:
    last = a
#print(last)
s = False
for i in nn:
    if s == False and i == last:
        ans += i
        s = True
    else:
        if i%10 == 0:
            ans += i
        else:
            ans += i + (10 - i%10)
    #print(ans)
print(ans)