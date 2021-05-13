X = int(input())

l = [1,2,3,4,5]
a = X // 100
b = X % 100

ans = 0
for i in l:
    if b % i == 0:
        if b // i <= a:
            ans = 1
            break

print(ans)