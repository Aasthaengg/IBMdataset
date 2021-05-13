a,b,k = map(int,input().split())
count = 0
for i in range(k):
    if a % 2 == 1:
        a -= 1
    a /= 2
    b += a
    count += 1
    if count == k:
        break
    if b % 2 == 1:
        b -= 1
    b /= 2
    a += b
    count += 1
    if count == k:
        break
print(str(round(a)) + " " + str(round(b)))