a, b, c = map(int, input().split())
count = 0
if a % 2 == 0 and a == b == c:
    print(-1)
    exit()

while a % 2 == 0 | b % 2 == 0 | c % 2 == 0:
    A = int((b + c) / 2)
    B = int((c + a) / 2)
    C = int((a + b) / 2)
    a = A
    b = B
    c = C
    count += 1
print(count)