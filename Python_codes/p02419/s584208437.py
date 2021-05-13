st=input()
count=0
while(True):
    s=input()
    if s=="END_OF_TEXT":
        break
    t=s.split()
    for k in t:
        if k.lower()==st:
            count+=1
print(count)