s=input()
sx,sy=map(str,s.split())
y1,y2=map(int,sy.split("."))

print(int(sx)*int(y1*100+y2)//100)
