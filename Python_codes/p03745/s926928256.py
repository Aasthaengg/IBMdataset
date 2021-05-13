N = int(input())
a = list(map(int,input().split()))

ans = 1

b= [a[0]]
if N > 1:
    for i in range(1,N):
        if a[i] != a[i-1]:
            b.append(a[i])

    if b[0] < b[1]:
        up_down = 1
    else:
        up_down = -1

i = 1
while i < len(b):
    if up_down*(b[i] - b[i-1]) < 0:
        ans += 1
        if b[i] < b[min(len(b)-1,i+1)]:
            up_down = 1
        else:
            up_down = -1
        i += 2
    else:
        i += 1

print(ans)