n=input()
x=0
for i in n:
    x+=int(i)
print("Yes" if x%9==0 else "No")