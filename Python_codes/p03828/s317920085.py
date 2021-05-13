import sys
sys.setrecursionlimit(2000)
n = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i,cnt])
    # 上のループを通した後にtempが1じゃなかったら、だけど、nが素数以外にそんなケースある？
    if temp!=1:
        arr.append([temp, 1])
    
    # 素数だったときの処理
    if arr == []:
        arr.append([n,1])

    return arr

factor_dict = {}
for i in range(2,n+1):
    factor_ls = factorization(i)
    for factor in factor_ls:
        if not factor[0] in factor_dict.keys():
            factor_dict[factor[0]] = 0
        factor_dict[factor[0]] += factor[1]
       
num_factor = 1
for num in factor_dict.values():
    num_factor *= num + 1
print(num_factor % (10**9 + 7))