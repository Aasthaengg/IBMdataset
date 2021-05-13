In = str(input())
Out = str(input())
cnt = 0
for i in range(len(In)):
  if In[i] != Out[i]:
    cnt += 1
    
    
print(cnt)