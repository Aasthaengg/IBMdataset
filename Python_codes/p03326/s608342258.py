n,m = map(int,input().split())

arr = []

for i in range(n):
    a,b,c = map(int,input().split())
    arr.append([a,b,c])

def tobin(x, n):
    return format(x, 'b').zfill(n)

ans = 0
for i in range(8):
    temp = tobin(i,3)
    buf = [0 for i in range(n)]
    for i in range(3):
        for j in range(n):
            if temp[i] == "0":
                buf[j] += -arr[j][i]
            else:
                buf[j] += arr[j][i]
    buf.sort(key=lambda x:-x)
    temp = 0
    for i in range(m):
        temp += buf[i]
    if temp > ans:
        ans = temp
print(ans)




