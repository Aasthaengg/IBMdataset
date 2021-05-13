n = int(input())
a = [0]*n
a = [int(input()) for i in range(n)]
if a[0] != 0:
    ans = -1
    

else:
    b = a[::-1]
    ans = 0
    for i in range(n-1):
        if abs(b[i] - b[i+1]) <= 1:
            if b[i] > b[i+1]:
                ans += 1
            else:
                ans += b[i]
            
        else:
            if b[i] < b[i+1]:
                ans += b[i]
            else:
                ans = -1
                break
print(ans)