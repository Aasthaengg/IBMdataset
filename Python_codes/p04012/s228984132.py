w = sorted(input())
count = 0
ans = 'Yes'
for i in range(len(w)-1):
  count += 1
  if w[i]!=w[i+1]:
    if count%2!=0:
      ans = 'No'
      break
    else:
      count = 0
print(ans if len(w)>1 else 'No')