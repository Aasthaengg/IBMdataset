k = int(input())
a, b = map(int, input().split())
if k - 1 <= b - a:
    print("OK")
else:
    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            break
    else:
        print("NG")