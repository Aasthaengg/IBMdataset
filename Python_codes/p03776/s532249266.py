import math
import sys
N, A, B = map(int, input().split())

v = list(map(int, input().split()))
v.sort()
    
def reduce(x):
  a = x[0]
  b = x[1]
  c = math.gcd(a,b)
  return (a//c, b//c)

def add_dict(dic, a, s):
  if a in dic:
    dic[a] += s
  else:   
    dic[a] = s
    
def comb(a, b):
  b = min(b, a-b)
  ans = 1
  for i in range(a,a-b,-1):
    ans *= i
  for j in range(1,b+1):
    ans //= j
  return ans

ct = {}
v.reverse()
sm = 0 #価値の和
i_prv = -1 #前回のvの値がでてくる最後の項数を示す
i_nxt = 0
search = True
dict_keys_list = []
for i in range(B):
  if search: # i_nxtを探す
    j = i
    while j < N-1 and v[j] == v[j+1]:
      j += 1
    i_nxt = j
    search = False
    
  sm += v[i]
  if A-1 <= i <= B-1: #品物はA個以上B個以下選ぶ
    add_dict(ct, reduce((sm, i+1)), comb(i_nxt-i_prv, i-i_prv))
    dict_keys_list.append(reduce((sm, i+1)))
    
  if i == i_nxt: #値が次に減る時は、i_prvを更新
    i_prv = i_nxt
    search = True
    

dict_keys_list.sort(key = lambda x: x[0]/x[1])
print(dict_keys_list[-1][0] / dict_keys_list[-1][1])
#print(dict_keys_list)
#print(ct)
print(ct[dict_keys_list[-1]])
  
    

