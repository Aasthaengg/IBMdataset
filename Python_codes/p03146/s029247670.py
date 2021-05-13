import sys

s = int(input())
a = []
a.append(s)
i = 1
while True:
    n = 0
    if a[i-1] %2 ==0:
        n = a[i-1]/2
    else:
        n = a[i-1]*3 +1
    i +=1
    if n in a:
        print(i)
        sys.exit()
    a.append(n)
