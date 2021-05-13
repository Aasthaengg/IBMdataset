n ,k = map(int, input().split())
s = input()
ret = ""
for i in range(n):
    if i==k-1:
        if s[k-1]=="A":
            ret += "a"
        elif s[k-1]=="B":
            ret += "b"
        elif s[k-1]=="C":
            ret += "c"
    else:
        ret += s[i]
print(ret)