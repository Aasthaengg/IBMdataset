def ceil(a0,b0):
  if a0%b0 == 0:
    return a0//b0
  else:
    return a0//b0 +1

t_num,a_num = 1,1

n = int(input())

for i in range(n):
    t,a = map(int,input().split())
    k = max(ceil(t_num,t),ceil(a_num,a))
    #その比に票を合わせる
    t_num = k*t
    a_num = k*a
    #print([t_num,a_num])    

print(t_num + a_num)
