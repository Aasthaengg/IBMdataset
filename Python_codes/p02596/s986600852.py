K = int(input())
 
sevens = 7 % K
count = 1
 
while(sevens % K !=0):
  # 計算桁を減らすために(mod K)で7, 77, 777,,,を計算する
  sevens = sevens * (10 % K) + (7 % K)
  sevens = sevens % K
  
  count += 1
  if count > K:
    count = -1
    break
    
print(count)