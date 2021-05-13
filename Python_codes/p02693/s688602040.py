k = int(input())
a, b = map(int, input().split())

while True:
    if a % k == 0:
        print("OK")
        break
    if a == b:
        print("NG")
        break
    a += 1