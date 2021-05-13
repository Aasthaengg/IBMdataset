import math
n = int(input())

# 素因数分解、辞書で返すやつ
# mathをimportする
def prime(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
        if num > n:
            break
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor

if n == 1:
    print(0)
    exit()

dic = {}
for a in range(1,n+1):
    pr = prime(a)
    for num, count in pr.items():
        if not num in dic.keys():
            dic[num] = count
        else:
            dic[num] += count
           
over = [0]*5
            
for num,count in dic.items():
    if count + 1 >= 75:
        over[0] += 1
    elif count + 1 >= 25:
        over[1] += 1
    elif count + 1 >= 15:
        over[2] += 1
    elif count + 1 >= 5:
        over[3] += 1
    elif count + 1 >= 3:
        over[4] += 1
        
for i in range(1,5):
    over[i] = over[i] + over[i-1]

ans = over[0]
ans += over[1] * (over[4]-1)
ans += over[2] * (over[3]-1)
ans += (over[4] - over[3]) * (over[3]*(over[3]-1)//2)
ans += over[3] * ((over[3]-1)*(over[3]-2)//2)

print(ans)