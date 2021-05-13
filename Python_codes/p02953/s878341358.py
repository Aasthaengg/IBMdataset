n = int(input())
a = list(map(int,input().split()))
flg = True

for i in range(n-2, -1, -1):
    if n == 1:
        break
    if a[i] - a[i+1] >= 2:
        flg = False
        break
    elif a[i] - a[i+1] == 1:
        a[i] -= 1
print('Yes') if flg else print('No')