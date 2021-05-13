s = list(map(str,input().split("/")))

if s[0] == "2017":
    s[0] = "2018"

print(s[0]+"/"+s[1]+"/"+s[2])