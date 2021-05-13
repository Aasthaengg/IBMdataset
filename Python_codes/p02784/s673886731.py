H,N = map(int, input().split())
data = list(map(int, input().split()))
S = 0
for i in range(0,len(data)):
    S += data[i]

if H > S:
    print("No")
else:
    print("Yes")