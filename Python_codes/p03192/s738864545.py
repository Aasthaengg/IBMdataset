n = int(input())
i = 0
flag = 0
m = [0,0,0,0]

m[0] = n // 1000
m[1] = n // 100 - m[0] * 10
m[2] = n // 10 - m[0] * 100 -  m[1] * 10
m[3] = n - m[0] * 1000 - m[1] * 100 - m[2] * 10

while i <= 3:
    if m[i] == 2 :
        flag = flag + 1
    i = i + 1
print(flag)