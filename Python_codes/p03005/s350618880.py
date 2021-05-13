n, k = (int(i) for i in input().split()) 


# 89 人　は一つしか貰えないが、１人は11個もらえる
 
others = k - 1  # 最大限に貰えないひとたちの人数
min_num = 1
max_num = n - others
 

if k < 2:
    print(0)
else:
    print(max_num - min_num)