x,a,b = map(int, raw_input().split())

if b <= a: print 'delicious'
elif b <= a + x: print 'safe'
else: print 'dangerous'
  
