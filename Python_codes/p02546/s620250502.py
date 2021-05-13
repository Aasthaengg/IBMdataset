n=list(input())
if n[len(n)-1]=="s":
  n.append("es")
else:
  n.append("s")
print("".join(n))
