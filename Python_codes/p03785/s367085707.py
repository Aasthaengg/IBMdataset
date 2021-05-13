n, c, k = map(int, input().split())
t = list()
for i in range(n):
    t.append(int(input()))
t.sort()
flag = 0
cnt = 0
state = 0
for i in range(0,n):
    if flag != 0:
        flag = flag - 1
        state = 0
    else:
        for j in range(0,min(c,n-i)):
            if t[i+j]-t[i] <= k and j == min(c-1,n-i-1): 
                cnt = cnt + 1
                flag = min(c-1,n-i-1)        
                state = 1
                break
            elif t[i+j]-t[i] <= k:
                state = 2
            elif t[i+j]-t[i] > k:
                cnt = cnt + 1
                flag = j-1
                state = 3
                break
print(cnt)