n = int(input())
h = list(map(int,input().split()))
h.reverse()
jud = 1
for i in range(n-1):
    if h[i] - h[i+1] == -1:
        h[i+1] -= 1
    elif h[i] - h[i+1] < -1:
        jud = 0
if jud == 1:
    print("Yes")
else:
    print("No")