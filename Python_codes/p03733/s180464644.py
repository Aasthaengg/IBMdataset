N,T = map(int,input().split())
t = list(map(int,input().split()))
dff_list = list()

if N == 1:
  print(T)
  exit(0)
  
for i in range(1,N):
  dff = t[i] - t[i -1]
  dff_list.append(dff)
  
ans_list = [T if T <= i else i for i in dff_list]

ans = sum(ans_list) + T
print(ans)