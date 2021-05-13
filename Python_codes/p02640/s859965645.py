X, Y = map(int,input().split())

ans = 'No'

#足が偶数であること
if Y%2 ==0:
    for i in range(X + 1):
        if (i * 2) + ((X - i) * 4) == Y:
            ans = 'Yes'
            break

print(ans)
