a,b = map(int,input().split())
s = max(0,4-a)*100000 +  max(0,4-b)*100000
if a==1 and b==1:
  s += 400000
print(s)