s=input()

if (s=="RRR"):
  print(3)
elif (s=="SRR" or s=="RRS"):
  print(2)
elif (s=="SSR" or s=="RSS" or s=="SRS" or s=="RSR"):
  print(1)
else:
  print(0)