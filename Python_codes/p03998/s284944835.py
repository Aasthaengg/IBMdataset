a = list(input()[::-1])
b = list(input()[::-1])
c = list(input()[::-1])

now = a
while len(now):
  next_ = now.pop()
  if next_ == 'a':now=a
  elif next_ == 'b':now=b
  else:now=c
    
print(next_.upper())