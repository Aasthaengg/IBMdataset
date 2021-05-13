s=input()
n=len(s)-1
l=[]
l3=[]
Sum=0
for i in range(2**n):
  bag=[" "]*n
  #print("pattern:",i)
  for j in range(n):
    if ((i>>j) & 1):
      bag[j]="+"
  l.append(bag)
#print(l)

for b in l:
  ll=[]
  inc=0
  for ii in range(n):
    if b[ii] == "+":
      ll.append(int(s[inc:ii+1]))
      inc=ii+1
  ll.append(int(s[inc:len(s)]))
  #print(ll)
  Sum+=sum(ll)
print(Sum)