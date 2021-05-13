s=[s for s in input()]
n=len(s)
print(max(ord(s[0])-ord('0')-1+9*(n-1),int(eval('+'.join(s)))))