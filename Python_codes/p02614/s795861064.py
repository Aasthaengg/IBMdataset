from  itertools import combinations as cmb
import copy 

H,W,K = map(int,input().split())

C = []
ans = 0

for i in range(H):
  C.append(list(input()))

for i in range(H):#選ぶ列数
  for j in range(W):#選ぶ行数
    for hs in cmb(range(H),i):#選ぶ列数の組み合わせ
      for ws in cmb(range(W),j):#選ぶ行数の組み合わせ
        tmpC = copy.deepcopy(C)#操作用配列
        for h in hs:
          tmpC[h] = ["" for k in range(W)]#その列を消す
        for w in ws:
          for k in range(H):
            tmpC[k][w]="" #その行を消す
        #print(tmpC,hs,ws,sum(tmpC,[]).count("#")==K)
        if sum(tmpC,[]).count("#")==K:
          ans +=1    
print(ans)