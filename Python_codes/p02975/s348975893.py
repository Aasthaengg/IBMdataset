from collections import Counter
n = int(input())
a = list(map(int,input().split()))
if sum(a)==0:
  print('Yes')
else:
  if n%3!=0:
    print('No')
  else:
    s = len(set(a))
    if s>3:
      print('No')
    else:
      l = Counter(a)
      tf = 1
      if s==3:
        for v in l.values():
          if v!=n//3:
            tf = 0
        li = list(set(a))
        if li[0]^li[1]^li[2]!=0:
          tf = 0
      elif s==2:
        if 0 not in l.keys():
          tf = 0
        else:
          for k in l.keys():
            if k==0 and l[k]!=n//3:
              tf = 0
      else:
        tf = 0
      print('Yes' if tf else 'No')