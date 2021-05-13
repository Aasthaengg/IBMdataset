A, B, T = list(map(int,input().split()))

a = 0
bis_num = 0
while True:
    a = a + A
    if a > T:
        break
    bis_num += B

print(bis_num)