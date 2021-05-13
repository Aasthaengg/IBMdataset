n,m = map(int,input().split())
if n > 1 and m > 1:
    num_9 = (n-2) * (m-2)
    ans = num_9
elif (n == 1) ^ (m == 1):
    if n == 1:
        num = m
    else:
        num = n
    ans = num - 2
else:
    ans = 1
print(ans)