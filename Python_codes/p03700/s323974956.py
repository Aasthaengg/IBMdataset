def check(M):
    global A,B,Data
    plus = 0
    for d in Data:
        left = d - B*M 
        if left > 0:
            q,mod = divmod(left,A-B)
            plus += q
            if mod > 0:
                plus += 1
    return plus <= M

N,A,B = map(int,input().split())
Data = [0]*N
for i in range(N):
    Data[i] = int(input())

min1 = 0
max1 = 10**10

while max1 - min1 > 1:
    mid = (min1 + max1) // 2
    b = check(mid)
    if b == True:
        max1 = mid
    else:
        min1 = mid

print(max1)
