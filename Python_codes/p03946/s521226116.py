import copy
 
n, t = map(int, input().split())
L = [int(i) for i in input().split()]

LL = [[0] for i in range(n)]
tmax = L[-1]
for i in range(n):
  if tmax <= L[-i-1]:
    tmax = L[-i-1]
  LL[-i-1] = tmax
 
minvalue = L[0]
maxvalue = LL[0]
subt = 0
count = 1
flag = 0
flagg = 0
j = 0
for i in range(n-1):
  if minvalue > L[i]:
    minvalue = L[i]
    flag = 1
  
  maxvalue = LL[i]
 
  #if maxvalue == L[i]:
    #LL = LL[i-j+1:]
    #maxvalue = max(LL)
    #j = i+1
 
  tsubt = maxvalue - minvalue
  if tsubt > subt:
    subt = tsubt
    count = 1
  elif tsubt == subt and flag == 1:
    count += 1
  flag = 0
  #print("L[i]:{0}, min:{1}, max:{2}, subt:{3}, count:{4}".format(L[i], minvalue, maxvalue, subt, count))
 
print(count)