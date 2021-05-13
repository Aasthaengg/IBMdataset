a, b, c = list(map(int, input().split()))

if (c<=b):
    print("delicious")
elif (c>b):
    if (c-b)<=a:
        print("safe")
    else:
        print("dangerous")