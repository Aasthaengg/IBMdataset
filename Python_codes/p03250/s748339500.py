s = "".join(input().split())
print(max(int(s[1:])+int(s[0]),int(s[:2])+int(s[-1]),int(s[-1]+s[0])+int(s[1])))