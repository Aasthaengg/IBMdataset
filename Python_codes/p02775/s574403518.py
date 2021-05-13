a=b=0
for n in map(int,'0'+input()):a,b=n+min(a,b),9-n+min(b,a+2)
print(min(a,b))