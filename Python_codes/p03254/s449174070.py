N,x = map(int,input().split())
a = list(map(int,input().split()))

a = sorted(a, reverse = False)

count = 0
if sum(a) < x:
    count = N -1
else:
    for i in a:
        x -= i
        if x < 0:
            break
        elif x == 0:
            count += 1
            break
        elif x > 0:
            count+=1

print(count)