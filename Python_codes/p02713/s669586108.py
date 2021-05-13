import math

def sum_of_gcd_of_tuples():
    # 入力
    K = int(input())
    # 初期処理
    sum_gcd = 0
    # 処理
    for a in range(1,K+1):
        for b in range(1,K+1):
            for c in range(1,K+1):
                gcd_num = math.gcd(a,b)
                gcd_num = math.gcd(gcd_num,c)
                sum_gcd += gcd_num
    return sum_gcd

result = sum_of_gcd_of_tuples()
print(result)