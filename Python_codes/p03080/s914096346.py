n=int(input())
s=str(input())
ans="Yes"
if s.count("R")<=s.count("B"):
    ans="No"
print(ans)