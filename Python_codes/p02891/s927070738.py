S = input()
K = int(input())

def calc(S):
  ret = 0
  seq = 1
  for i in range(1,len(S)):
    if S[i-1] == S[i]:
      seq += 1
    else:
      ret += seq // 2
      seq = 1
  ret += seq // 2
  return ret
## pK + q（K-1)  として解けるきがします
## pK + q


if S[0] * len(S) == S:
  # 全部おなじだったら
  print((len(S) * K) // 2)
elif K < 1000:
  print(calc(S*K))
else:
  x1 = calc(S)    # p+q
  x2 = calc(S*2)  #2p+q
  print((x2-x1) * K + 2*x1 - x2)
  
