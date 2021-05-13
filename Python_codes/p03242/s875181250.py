s=input()
n=""
for i in s:
    if i=="1":
        n+="9"
    elif i=="9":
        n+="1"
    else:
        n+=i
print(n)
