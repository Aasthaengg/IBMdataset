# -*- coding: utf-8 -*-
import sys

N = int(input().strip())
#-----


class factorization():
    def get_divisor(self, n :int) -> dict:
        divisor_dic={}
        
        tmp_num = n
        for i in range(2,n):
            while tmp_num % i == 0:
                divisor_dic.setdefault(i,0)
                divisor_dic[i] += 1
                
                tmp_num //= i
        
        return divisor_dic


divisor_dic={}  # 階乗を素因数分解し、結果を入れる
for num in range(2,N+1):
    # 階乗の、それぞれの数字について、約数を抽出
    fa = factorization()
    ret = fa.get_divisor(num)

    for key,v in ret.items():
        divisor_dic.setdefault(key,0)
        divisor_dic[key] += v
    
    divisor_dic.setdefault(num,0)
    divisor_dic[num] += 1


cnt_divisor_dic={ i:0 for i in [74,24,14,4,2]}
# 約数の個数が74以上、24,14,4,2以上、で場合分けし、件数を集計
for key,v in divisor_dic.items():
    for j in [74,24,14,4,2]:
        if v >= j:
            cnt_divisor_dic[j] += 1


# 75=5*5*3　をもとに、すべての組み合わせを考え、合計する。
# 75
# 25 × 3(選択した「25以上」の約数は、「3以上」の約数でもあるため、1引いておく)
# 15 × 5(選択した「15以上」の約数は、「5以上」の約数でもあるため、1引いておく)
# 5×5×3 (「5以上」の約数から2つ選択する組み合わせxC2)
sum = cnt_divisor_dic[74] + \
      cnt_divisor_dic[24] * (cnt_divisor_dic[2] - 1) + \
      cnt_divisor_dic[14] * (cnt_divisor_dic[4] - 1) + \
      cnt_divisor_dic[4] * (cnt_divisor_dic[4] - 1) // (2*1) * (cnt_divisor_dic[2] - 2)

print(sum)
