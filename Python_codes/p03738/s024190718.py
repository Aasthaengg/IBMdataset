a,b=int(input()),int(input())
l=["EQUAL","GREATER","LESS"]
if a>b:
  ans="GREATER"
elif a<b:
  ans="LESS"
else:
  ans="EQUAL"
print(ans)