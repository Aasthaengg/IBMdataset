text=str(input())
t=''
for i in text:
    if i.isupper()==True:
        t+=i.lower()
    else:
       t+=i.upper()

print(t)
