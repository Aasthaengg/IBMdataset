abcdek=[]
for i in range(6):
  abcdek.append(int(input()))
ans="Yay!"
k=abcdek[5]
for i in range(5):
  p=abcdek[i]
  for j in range(i+1,5):
    q=abcdek[j]
    if q-p>k:
      ans=":("
      break
print(ans)