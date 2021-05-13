def resolve():
   l=list(map(int, input().split()))
   a=l.count(1)
   b=l.count(9)
   c=l.count(7)
   d=l.count(4)
   if a==b==c==d==1:
       print('YES')
   else:
       print('NO')
resolve()