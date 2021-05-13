def LI():
    return list(map(int, input().split()))


X, Y = LI()
a = 10**18//X
if X == Y:
    ans = -1
elif X % Y == 0:
    ans = -1
else:
    for i in range(2, a+1):
        if X*i % Y == 0:
            continue
        ans = X*i
        break
print(ans)
