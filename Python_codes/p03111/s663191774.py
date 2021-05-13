import itertools

N,A,B,C = map(int,input().split())
Comb = itertools.product([0,1,2,3],repeat=N)

L = []
for i in range(N):
  l = int(input())
  L.append(l)
  
# 各竹について  
# 0 : 使用しない
# 1 : 竹Aの材料にする  
# 2 : 竹Bの材料にする 
# 3 : 竹Cの材料にする
# 竹A,B,Cの作成法 :
# とりあえず全部合成 → 目的の長さに合わせる

ans = float('inf')
for X in Comb:
  tmp = 0
  m_A,m_B,m_C = [],[],[]
  for i in range(N):
    if(X[i] == 1): m_A.append(L[i])
    elif(X[i] == 2): m_B.append(L[i])
    elif(X[i] == 3): m_C.append(L[i])
  # 空の竹リストがないなら    
  if(len(m_A)*len(m_B)*len(m_C) != 0):      
    for take_list,take_len in zip([m_A,m_B,m_C],[A,B,C]):
      tmp += (len(take_list)-1)*10 # 合成
      tmp += (abs(take_len-sum(take_list)))*1 # 延長or短縮
    ans = min(ans,tmp)
  
print(ans)  