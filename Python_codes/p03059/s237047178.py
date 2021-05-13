
a = list(map(int, input().split()))

A = a[0]
B = a[1]
T = a[2]

cout = 0
loopCount = 1
timeOut = T + 0.5
time = A
while True:
    if time >= timeOut:
        break
    cout += B
    loopCount += 1
    time = A * loopCount

print(cout)