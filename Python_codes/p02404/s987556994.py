ret = ''
while True:
   h,w = map(int, raw_input().split())
   if h == w == 0: 
       break   
   ret += '#'*w+'\n'
   ret += ('#' + '.' * (w-2) + '#\n') * (h - 2)
   ret += '#'*w+'\n\n'
print ret, 