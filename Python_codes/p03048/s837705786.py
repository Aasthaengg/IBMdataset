colorn = list(map(int, input().split()))
color = colorn[0:3]
n = colorn[-1]
color.sort()

a, b, c = color[2], color[1], color[0]

a_max = n // a
cnt = 0
ip, jp, kp = -1, -1, -1

for i in range(a_max + 1):
    b_max = (n - a * i) // b
    d = n - a * i
    flag = 0
    for j in range(b_max + 1):
        c_max = (n - a * i - b * j) // c
        for k in range(c_max, c_max + 2):
            if a * i + b * j + c * k == n:
                cnt += 1
                if ip == i:
                    dj = j - jp
                    cnt += ((d // b - j) // dj)
                    flag = 1
                    break
                else:
                    ip, jp, kp = i, j, k
            elif a * i + b * j + c * k > n:
                break
        if flag == 1:
            break
print(cnt)