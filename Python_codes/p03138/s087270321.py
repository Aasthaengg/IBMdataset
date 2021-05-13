n,k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]


for i in range(len(a)):
    a[i] = '{:040b}'.format(a[i])
p = len(bin(k))-2
k = '{:040b}'.format(k)
ans = 0
for i in range(0,40-p):
    num_1 = 0
    num_0 = 0
    for j in range(n):
        if a[j][i] == '1':
            num_1 += 1
        elif a[j][i] == '0':
            num_0 += 1
    num = num_1
    ans += (2**(39-i))*num

t = True
for i in range(40-p,40):
    num_1 = 0
    num_0 = 0
    if t:
        if k[i] == '1':
            for j in range(n):
                if a[j][i] == '1':
                    num_1 += 1
                elif a[j][i] == '0':
                    num_0 += 1
            if num_0 > num_1:
                num = num_0
                ans += (2**(39-i))*num
            else:
                t = False
                num = num_1
                ans += (2**(39-i))*num
        elif k[i] == '0':
            for j in range(n):
                if a[j][i] == '1':
                    num_1 += 1
                elif a[j][i] == '0':
                    num_0 += 1
            num = num_1
            ans += (2**(39-i))*num
    else:
        for j in range(n):
            if a[j][i] == '1':
                num_1 += 1
            elif a[j][i] == '0':
                num_0 += 1
        if num_0 > num_1:
            num = num_0
            ans += (2**(39-i))*num
        else:
            num = num_1
            ans += (2**(39-i))*num
print(ans)