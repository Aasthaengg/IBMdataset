import math
import random

def is_prime3(q,k=50):
    q = abs(q)
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    #判定をk回繰り返す
    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def get_prime(number):
    prime_list = []
    search_list = list(range(2,number + 1))
    while search_list[0] <= math.sqrt(number):
        head_num = search_list.pop(0)
        prime_list.append(head_num)
        search_list = [num for num in search_list if num % head_num != 0]
    prime_list.extend(search_list)
    return prime_list

l = get_prime(10**6+10)
N = int(input())
ans = 0
k = 1
i = 0
l2 = []
while(l[i]**2 <= N):
    if N % (l[i]**k) == 0:
        N //= (l[i]**k)
        l2.append(l[i]**k)
        k += 1
        ans += 1
    else:
        i += 1
        k = 1
index = 0
while(index < len(l2)):
    if N % (l2[index]) == 0:
        N //= l2[index]
    else:
        index += 1
if is_prime3(N) and N not in l2:
    ans += 1
print(ans)
