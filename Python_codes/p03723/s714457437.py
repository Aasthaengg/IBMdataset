a, b, c = map(int,input().split())
count = 0
def exchange(a, b, c, count):
    a, b, c = int((b+c)/2), int((a+c)/2), int((a+b)/2)
    count += 1
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        return a, b, c, count
    else:
        return exchange(a, b, c, count)
if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    print(0) 
elif a == b == c:
    print(-1)
else:
    aa, bb, cc, count = exchange(a, b, c, count)
    print(count)