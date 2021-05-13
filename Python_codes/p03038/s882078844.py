n,m = map(int,input().split())
a_list = list(map(int,input().split()))
a_list.sort()
b_c_list = []
for i in range(m):
  b_c_list.append(list(map(int,input().split())))

b_c_list.sort(key=lambda x: x[1],reverse = True)
                  
count = 0
d = []
for b_c in b_c_list:
  for i in range(b_c[0]):
    d.append(b_c[1])
    count += 1
    if count >= n:
      break
  if count >= n:
    break
    

for i in range(min(n,len(d))):
  if a_list[i] < d[i]:
    a_list[i] = d[i]
  else:
    break
    
print(sum(a_list))