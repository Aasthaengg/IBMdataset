n=list(input())
cindex=[i for i,j in enumerate(n) if j=="C"]
findex=[i for i,j in enumerate(n) if j=="F"]
if ("C" in n and "F" in n) and (min(cindex)<max(findex)):
    print("Yes")
else:
    print("No")