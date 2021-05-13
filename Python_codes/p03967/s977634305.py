g,p,w,l=0,0,0,0
for s in input():
  if s=="g":
    if g>p:
      p+=1
      w+=1
    else:
      g+=1
  else:
    if g>p:
      p+=1
    else:
      g+=1
      l+=1

print(w-l)