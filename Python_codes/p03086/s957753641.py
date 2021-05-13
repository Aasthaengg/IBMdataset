n=[*'ACGT'];s=input();count,result=0,0
for i in range(len(s)):
  for j in range(i,len(s)):
    if s[j] not in n:
      break
    else:
      count+=1
  result=max(result,count)
  count=0
print(result)