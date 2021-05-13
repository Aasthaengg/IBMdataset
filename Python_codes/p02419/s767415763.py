W=input()

Ti=[]
count=0

while True:
  T=input()
  s=T.lower()
  if T=="END_OF_TEXT":
    break
  Ti += list(s.split())

  
for i in range(len(Ti)):
  if Ti[i]==W:
    count +=1

print(count)
