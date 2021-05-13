def joinstring(O, E) : 
  if len(O) - len(E) > 0 : 
    str = "".join([i + j for i, j in zip(O, E)])
    str += O[-1]
    return str
  else : 
    str = "".join([i + j for i, j in zip(O, E)])
  return str


O = input()
E = input()

print(joinstring(O, E))