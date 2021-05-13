N,T = map(int,input().split())
List = list(map(int,input().split()))
dic = {}
min = List[0]
for i in range(N):
  if List[i]<min:
    min = List[i]
  if List[i]-min not in dic:
    dic[List[i]-min] = 1
  else:
    dic[List[i]-min] += 1
dic2 = sorted(dic.items(), reverse=True)
Answer = dic2[0][1]
print(Answer)