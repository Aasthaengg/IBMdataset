n = int(input())
s = [int(input()) for _ in range(n)]
tots = sum(s)
if tots % 10 > 0:
   print(tots)
else:
   t = [x for x in s if x % 10 > 0]
   if len(t) == 0:
      print(0)
   else:
      t.sort()
      print(tots-t[0])
