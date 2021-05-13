X, A, B = map(int, input().split())
mypoint = 0
if mypoint-A+B<=mypoint:
    print("delicious")
elif mypoint-A+B<=X:
    print("safe")
else:
    print("dangerous")