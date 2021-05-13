n = int(input())
dic = {}
for i in range(2, n+1):
    num = i
    for j in range(2, num+1):
        c = 0
        while num%j==0:
            c += 1
            num //= j
        if c > 0:
            if j in dic:
                dic[j] += c
            else:
                dic[j] = c
t, f, ft, tw = 0,0,0,0
end = 0
for _i, j in dic.items():
    if j >= 2:
        t += 1
        if j >= 4:
            f += 1
            if j >= 14:
                ft += 1
                if j >= 24:
                    tw += 1
                    if j >= 74:
                        end += 1

result = 0

result += end

result += tw*(t-1)

result += ft*(f-1)

result += f*(f-1)*(t-2)//2

print(result)