a, b, c = list(map(int, input().split()))
if a == b == c and a % 2 == 0:
    print(-1)
    exit()
count = 0
while True:
    if sum([a % 2, b % 2, c % 2]) > 0:
        print(count)
        exit()
    else:
        a, b, c = (b + c) // 2, (a + c) // 2, (a + b) // 2
        count += 1