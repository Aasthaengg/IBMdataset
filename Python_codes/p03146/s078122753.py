n=int(input())
a=[n];count=0
while True:
  if a[count]%2==0: b=a[count]//2
  else: b=3*a[count]+1
  if b in a:
    print(len(a)+1)
    exit()
  a.append(b)
  count+=1