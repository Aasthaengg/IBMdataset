n=input()
result=''
n=str(n)
for i in n:
    if i=='9':
        result+='1'
    elif i=='1':
        result+='9'
print(result)
