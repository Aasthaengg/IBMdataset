s = list(input().split("/"))
answer = "TBD"

if int(s[0]) <= 2019:
  if int(s[1]) <= 4:
    if int(s[2]) <= 30:
      answer = "Heisei"
      
print(answer)