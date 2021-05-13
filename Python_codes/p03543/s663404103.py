n=input()
a=0
for i in range(2):
  if n[i]==n[i+1] and n[i+1]==n[i+2]:
    a=1
print(["No","Yes"][a])
