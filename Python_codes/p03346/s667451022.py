N = int(input())
temp = [0 for x in range(N+1)]

#既に昇順に並んでいる最も長い部分列を考えて、残りの部分を動かす
#ex.[5,6,1,2,3,4]→4 [1,3,2,4]→2(12 or 34) [6,3,1,2,7,4,8,5]→3(678)

#tempに各数値を基準にした昇順の部分列をリストにし、MAX（最も長い部分列）を取る

for i in range(N):
  X=int(input())
  temp[X]=temp[X-1]+1
  
print(N-max(temp))