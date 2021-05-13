n = input()
count=0
m = 0
for s in n:
  if s =="A" or s == "C" or s == "G" or s== "T" :
    count+=1
    m =max(m,count)
  else:
    count=0
print(m)