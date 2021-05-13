a,b,c = map(int,input().split())
d = int(input())
count = 0
while True:
    if a < b:
        if b < c:
            break
        else:
            c *= 2
            count += 1
    else:
        b *= 2
        count += 1
print("Yes" if count <= d else "No")