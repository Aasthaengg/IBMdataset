k,t = map(int,input().split())
a = list(map(int,input().split()))
b = [0]*t
for i in range(t):
    b[i] = [a[i], i]
s = -1
ans = 0
if t == 1:
    ans = k-1
else:
    for i in range(k):
        b.sort(key= lambda val : val[0],reverse=True)
        if b[0][1] == s:
            if b[1][0] == 0:
                ans = b[0][0]
                break
            else:
                b[1][0] -= 1
                s = b[1][1]
        else:
            b[0][0] -= 1
            s = b[0][1]
print(ans)