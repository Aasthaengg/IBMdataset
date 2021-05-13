S=input()
if ("R" in S) and ("RR" not in S) and ("RRR" not in S):
  print(1)
elif ("RR" in S) and ("RRR" not in S):
  print(2)
elif ("RRR" in S):
  print(3)
else:
  print(0)