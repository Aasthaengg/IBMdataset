n = int(input())
x = sorted(list(map(int, input().split())), reverse = True)
x_2 = list(map(lambda x:x ** 2, x))
ichi = sum(x)
jijou = sum(x_2)
re = 10 ** 100


#def ji(p, x):
#    ans = p * (p - 2 * x)
#    return ans

for p in range(1, x[0] + 1):
    second = n * (p ** 2)
    third = -2 * p * ichi
    summ = jijou + second + third

    if re > summ:
        re = summ

print(re)

#for i in range(x[i]):
