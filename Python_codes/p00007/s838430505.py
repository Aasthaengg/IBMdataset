n = int(raw_input())

m = 100000

for x in range(n) :
  m = int(m*1.05)
  
  if m % 1000 :
    m = (m/1000)*1000+1000
print m