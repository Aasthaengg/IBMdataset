from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

n,k = map(int,input().split())
a = list(map(int,input().split()))

bit_sum = [0]*40
keta = [0]*40

for i in a:
    for j in range(40):
        if i&2**j == 2**j:
            bit_sum[j] += 1

k_bit = [0]*40
flag = False

for i in range(40):
    if k&2**i == 2**i:
        k_bit[i] = 1

def count(ke,flag):
    if ke == -1:
        return 0
    if k_bit[ke] == 1:
        if flag:
            return max(2**ke*bit_sum[ke],2**ke*(n-bit_sum[ke]))+count(ke-1,flag)
        else:
            if 2**ke*(n-bit_sum[ke]) > 2**ke*bit_sum[ke]:
                return 2**ke*(n-bit_sum[ke])+count(ke-1,flag)
            else:
                flag = True
                return 2**ke*bit_sum[ke]+count(ke-1,flag)
    else:
        if flag:
            return max(2**ke*bit_sum[ke],2**ke*(n-bit_sum[ke]))+count(ke-1,flag)
        else:
            return 2**ke*bit_sum[ke]+count(ke-1,flag)

print(count(39,False))