from collections import defaultdict
dic = defaultdict(int)
N,M = map(int,input().split())
A = list(map(int,input().split()))
for x in A:
  dic[x] += 1
for i in range(M):
  a,b = map(int,input().split())
  dic[b] += a

#print(dic)
L =list(dic.keys())
L.sort(reverse = True)

cnt = 0
ans = 0
for i in range(len(L)):
  val = L[i]
  #print(cnt,val,dic[val])
  if cnt + dic[val] <= N:
    cnt += dic[val]
    ans += val*dic[val]
  else:
    ans += val*(N-cnt)
    break
print(ans)
