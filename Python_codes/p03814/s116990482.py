import sys
s = str(input())

for i in range(len(s)):
  if s[i]=="A":
    for j in range(1,len(s)):
      if s[-1*j]=="Z":
        print(len(s)-i-j+1)
        sys.exit()