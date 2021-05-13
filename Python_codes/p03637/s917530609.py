n = int(input())
a = list(map(int, input().split()))
o = 0
t = 0
f = 0
for i in range(n):
    if a[i]%4 == 0:
        f += 1
    elif a[i]%2 == 0:
        t += 1
    else:
        o += 1
if t == 0:
    if f+1 >= o:
        print("Yes")
    else:
        print("No")
else:
    if f >= o:
        print("Yes")
    else:
        print("No")