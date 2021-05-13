N = int(input())

dic = {}

for _ in range(N):
  s = input()
  s = sorted(s)
  s = "".join(s)
  if s not in dic:
    dic[s] = 1
  else:
    dic[s] +=1
  
rlt = 0
for k in dic:
  rlt += dic[k]*(dic[k]-1)//2
  
print(rlt)