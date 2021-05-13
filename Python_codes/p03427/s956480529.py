s=input()
print(max(sum(map(int,list(s))),int(s[0])-1+9*len(s)-9))