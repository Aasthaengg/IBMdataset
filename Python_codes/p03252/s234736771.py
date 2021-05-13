S = str(input())
T = str(input())

exchange = [-1] * 26
alpha2num = lambda c: ord(c) - ord('a')
#print(alpha2num('y')) #==> 24

for i in range(len(S)):
    now_num = alpha2num(S[i])
    #print(now_num, exchange[now_num], alpha2num(T[i]))
    if exchange[now_num] == -1:
      exchange[now_num] = alpha2num(T[i])
    elif exchange[now_num] == alpha2num(T[i]):
      #print("yeee")
      continue
    else:
      print("No")
      quit()
  #print(exchange)    
  
exchange = sorted(exchange)
for i in range(1, 26):
  if exchange[i] == exchange[i - 1]:
    if exchange[i] != -1:
      print("No")
      quit()
  
print("Yes")
