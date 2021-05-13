import sys
for e in sys.stdin:
 a,b=list(map(int,e.split()));p=a*b
 while b:a,b=b,a%b
 print(a,p//a)
