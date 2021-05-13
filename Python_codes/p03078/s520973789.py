x,y,z,k = map(int,input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))
a_list.sort(reverse = True)
b_list.sort(reverse = True)
c_list.sort(reverse = True)
def check(p):
  count = 0
  for i in range(x):
    for j in range(y):
      for m in range(z):
        if a_list[i] + b_list[j] + c_list[m] < p:
          break
        count += 1
        if count >= k:
          return True
  return False

left = 1
right = 10**20
while right - left > 1:
  middle = (right + left)//2
  if check(middle) == True:
    left = middle
  else:
    right = middle
ans_list = []
for i in range(x):
    for j in range(y):
      for m in range(z):
        if a_list[i] + b_list[j] + c_list[m] < left +1:
          break
        elif a_list[i] + b_list[j] + c_list[m] >= left+1:
          ans_list.append(a_list[i] + b_list[j] + c_list[m])
nokori = k - len(ans_list)
for i in range(nokori):
  ans_list.append(left)
  
ans_list.sort(reverse = True)
for ans in ans_list:
  print(ans)
          
