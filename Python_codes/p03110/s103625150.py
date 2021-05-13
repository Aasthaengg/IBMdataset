N = int(input())
money, type = [], []
for i in range(N):
    m, t = input().split()
    money.append(float(m))
    type.append(t)

sum = 0
for i in range(N):
    if type[i] == 'JPY':
        sum += money[i]
    else :
        sum += money[i]*3.8*10**5
print(sum)