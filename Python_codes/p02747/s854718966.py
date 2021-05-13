S = input()
outputString = "No"
if len(S) % 2 !=0:
 outputString="No"
else:
  outputString = "Yes"
  for k,v in enumerate(S):
    if (k % 2 == 0 and v!="h") or (k % 2 == 1 and v!="i"):
       outputString = "No"
       break

print(outputString)
