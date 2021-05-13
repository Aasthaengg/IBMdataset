s=list(str(input()))

if s.count("1") >= s.count("0"):
  print(2*s.count("0"))
elif s.count("1") < s.count("0"):
  print(2*s.count("1"))