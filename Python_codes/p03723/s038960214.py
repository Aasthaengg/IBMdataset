a,b,c = map(int,input().split())
if a%2 == 1 or b%2 == 1 or c%2== 1 :
    print(0)
    exit()
elif a == b and b == c :
    print(-1)
    exit()
count = 0
while (a%2 == 0 and b%2 == 0 and c%2 == 0) :
    count += 1
    x = (a+b)/2
    y = (b+c)/2
    z = (c+a)/2
    a = x
    b = y
    c = z


print(count)