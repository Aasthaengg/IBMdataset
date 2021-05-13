s = input() 
t = s[::-1]
l = s.index("A")
r = t.index("Z") 
ans = len(s) - l - r 
print(ans)