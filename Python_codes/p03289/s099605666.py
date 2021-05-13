s = input()
ans = "WA"

if s[0] == "A" and s[2:-1].count("C") == 1:
  tmp = s[1:]
  tmp = tmp.replace("C","")
  ans = "AC" if tmp.islower() else "WA"
  
print(ans)