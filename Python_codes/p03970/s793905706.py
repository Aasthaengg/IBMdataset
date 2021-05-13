c = 'CODEFESTIVAL2016'
s = input()

co = 0

for i in range(len(c)):
  if s[i] != c[i]:
    co += 1
    
print(co)