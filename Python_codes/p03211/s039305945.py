s = list(open(0).read().rstrip())

print(min([abs(753-int(s[i]+s[i+1]+s[i+2])) for i in range(len(s)-2)]))