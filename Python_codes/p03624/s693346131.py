alphabeta = "abcdefghijklmnopqrstuvwxyz"
all_str  = set(alphabeta) 
str = input() 
str = set(str)


use = all_str-str 
if use == set():
  print("None")
else:
  print(sorted(use)[0])