s=input()
result=''
for i in s:
    if i==',':
        result+=' '
    else:
        result+=i
print(result)