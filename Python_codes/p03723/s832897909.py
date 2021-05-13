A, B, C = list(map(int, input().split()))
cookies = set()
cookies.add((A, B, C))

a = A
b = B
c = C

count = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    count += 1
    a = a // 2
    b = b // 2
    c = c // 2
    
    a2 = b + c
    b2 = a + c
    c2 = b + c
    if (a2, b2, c2) in cookies:
        count = -1
        break
    a = a2
    b = b2
    c = c2
    cookies.add((a, b, c))
print(count)