n,r = map(int,input().split())
rate = 0
 
if n<10:
  rate = r + 100*(10-n)
elif n>=10:
  rate = r
  
print(rate)