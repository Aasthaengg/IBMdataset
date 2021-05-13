N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

excess = 0
for i in range(N):
    dif = a[i]-b[i]
    if dif < 0:
        excess += abs(dif)//2
    elif 0 < dif:
        excess -= dif

if 0<=excess:
    print("Yes")
else:
    print("No")