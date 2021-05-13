def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

s=input()
t=input()
c=0
for i in range(len(s)):
    if s[i]!=t[i]:
        c+=1
print(c)





