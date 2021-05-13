s=list(input())
n=len(s)
l=list("abcdefghijklmnopqrstuvwxyz")
l.append("None")
for i in range(n):
    if s[i] in l:
        l.remove(s[i])
print(l[0])

    
