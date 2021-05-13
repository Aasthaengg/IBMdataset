N=int(input())
P = [0] * N
for i in range(N):
  P[i] = int(input())
  
# 差1で作れるもっとも長い部分列の長さをNから引く
# 例：1 3 2 4 -> 1,2もしくは3,4が最も長い
# 例：3 2 5 1 4 6 -> 3,4もしくは5,6
# 例：6 3 1 2 7 4 8 5 -> 6,7,8もしくは3,4,5もしくは1,2

seen=[0 for i in range(N+1)]
for i in range(N):
  # P[i]より1小さい数が今までに出てきていたら、その数に+1する。
  seen[P[i]] = seen[P[i] - 1] + 1
  
print(N - max(seen))
