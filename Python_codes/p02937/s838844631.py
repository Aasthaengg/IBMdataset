S = input()
T = input()
dic = {}
for i,s in enumerate(S):
  if s not in dic:
    dic[s] = [i]
  else:
    dic[s].append(i)
#print(dic)
ind = -1
loop = 0
import bisect
for t in T:
  if t not in dic:
    ans = -1
    break
  if dic[t][-1]<=ind:
    loop += 1
    ind = dic[t][0]
  else:
    i = bisect.bisect_right(dic[t],ind)
    ind = dic[t][i]
  #print(ind)
#print(loop,ind)
else:
  ans = len(S)*loop+ind+1
          
print(ans)   

#print(*ans[1:], sep='\n')
