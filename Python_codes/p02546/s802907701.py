s = list(input().strip())
len_s = len(s)
if s[len_s-1] == "s":
    s += "es"  
else:
    s += "s"
s= "".join(s)
print(s)