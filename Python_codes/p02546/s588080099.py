s = list(input())

es = list("es")
ss = list("s")

#print(len(s))


f = s[len(s)-1]
#print(f)

if f == "s":
  ans = s+es
  ans = "".join(ans)
  print(ans)
else:
  ans = s+ss
  ans = "".join(ans)
  print(ans)
  
