import sys
s=sys.stdin.read().lower()

for i in range(26):


    s.count(chr(97+i))

    print(chr(97+i)+" : "+str(s.count(chr(97+i))))

    


