abc = list(map(int,input().split()))
abc.sort()
a = abc[0]
b = abc[1]
c = abc[2]
count = 0
x = c-b
a += x
b += x
count += x
if not (b-a) % 2 == 0:
    b += 1
    c += 1
    count += 1
x = (b-a)//2
a += (b-a)
count += x
print(count)