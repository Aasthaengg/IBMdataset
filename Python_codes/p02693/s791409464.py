k = int(input())
a, b = [int(i) for i in input().split()]

if(a % k == 0):
    print("OK")
else:
    if(a // k != b // k):
        print("OK")
    else:
        print("NG")