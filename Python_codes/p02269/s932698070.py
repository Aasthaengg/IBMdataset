n = input()
dic = set()
 
for i in range(n):
  com, st = map(str, raw_input().split())
  if com == 'insert':
    dic.add(st)
  elif com == 'find':
    if st in dic:
      print 'yes'
    else:
      print 'no'