def reducestr(s) : 
  return s[0] + str(len(s[1 : len(s) - 1])) + s[-1]

s = input()

print(reducestr(s))