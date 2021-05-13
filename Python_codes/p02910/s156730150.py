s=input()
n=len(s)
odd=[s[i] for i in range(0,n,2)]
even=[s[i] for i in range(1,n,2)]
if "L" in odd:
  print("No")
elif "R" in even:
  print("No")
else:
  print("Yes")