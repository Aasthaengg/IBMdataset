n=int(input())

print(0)
lowg = input()
print(n-1)
highg = input()

if lowg=="Vacant":
  quit()
if highg=="Vacant":
  quit()

low =0 
high=n-1
mid = (n-1)//2
for i in range(20):
  print(mid)
  temp=input()
  if temp=="Vacant":
    quit()
  if (mid-low)%2==0:
    if lowg==temp:
      lowg=temp
      low=mid
    else:
      high=mid
  else:
    if lowg==temp:
      high=mid
    else:
      lowg=temp
      low=mid
  #print("high " + str(high) + " low "+str(low))
  mid=(high+low)//2