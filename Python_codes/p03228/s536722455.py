a,b,c = map(int,input().split(" "))
count = 0
t = "A"
while True:
    count += 1
    if t == "A":
        b += a // 2
        a //= 2
        t = "B"
    else:
        a += b // 2
        b //= 2
        t = "A"
    if count == c:
        print(a,b)
        exit()
    elif a * 2 == b or b * 2 == a:
        break
if (c - count) % 2 == 0:
    print(a,b)
else:
    print(b,a)