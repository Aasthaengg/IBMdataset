H,A=map(int,input().split())
result=0
if H%A==0:
    result=H/A
else:
    result=H//A+1
print(int(result))