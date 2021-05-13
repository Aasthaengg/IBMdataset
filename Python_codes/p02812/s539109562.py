n = int(input())

s = input()
a = [str(c) for c in s]

c = 0

for i in range(n-2):
  if a[i] == 'A' and a[i+1] == 'B' and a[i+2] == 'C':
    c +=1
  else:
    continue
    
print(c)

