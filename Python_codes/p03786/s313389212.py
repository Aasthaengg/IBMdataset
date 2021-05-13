n = int(input())
a = list(map(int, input().split()))
a.sort()
sm = 0
r = [0]*n
r[0]=a[0]
for i in range(1,n):
    if r[i-1]*2 >= a[i]:
        sm += 1
    else:
        sm = 0
    r[i] = r[i-1] + a[i]

print(sm+1)