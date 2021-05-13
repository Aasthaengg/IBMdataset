s = input()
t = input()

sl = list(s)
tl = list(t)

count = 0

for (a, b) in zip(sl, tl):
  if a!=b:
    count+=1
    
print(count)
