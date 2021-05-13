a = int(input())
b = int(input())
c = int(input())
x = int(input())
x /= 50
cnt = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 10*i + 2*j + k == x:
                cnt += 1
print(cnt)