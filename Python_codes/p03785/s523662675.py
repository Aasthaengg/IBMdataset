n, c, k = map(int, input().split())
p = [0 for i in range(n + 1)]
t0 = [int(input()) for i in range(n)]
t0.sort()
t = []
for i in range(n):
    temp = t0[i]
    t.append([temp, 1, i])
    t.append([temp + k, 2, i])
t.sort()
count = 0
for i in t:
    num = i[2]
    if i[1] == 1:
        p[num] += 1
    else:
        num2 = (p[num] - 1) // c + 1
        count += num2
        temp = num + 1
        num3 = c * num2 - p[num]
        while num3 > 0:
            if p[temp] == 0:
                break
            else:
                num4 = min(num3, p[temp])
                num3 -= num4
                p[temp] -= num4
                temp += 1
        p[num] = 0
print(count)