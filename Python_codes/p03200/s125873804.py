s=input()
val=0
b=0
for c in s:
    if c=='B':
        b+=1
    else:
        val+=b
print(val)