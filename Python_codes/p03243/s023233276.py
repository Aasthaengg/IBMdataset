a=[111,222,333,444,555,666,777,888,999]

n=int(input())

for i in a:
  if n>i:
    continue
    
  else:
    print(i)
    exit()