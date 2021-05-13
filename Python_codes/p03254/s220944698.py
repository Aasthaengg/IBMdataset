n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

i = 0
while True:
    x = x - a[i]
    if x >= 0 and i+1 != len(a):
        i += 1
    elif x == 0 and i+1 == len(a):
        i += 1
        break
    else:
        break

print(i)