w=input().lower()
count=0
while True:
    t=input()
    if t=='END_OF_TEXT':
        break
    t=t.lower().split()
    for i in t:
        if w==i:
            count+=1
print(count)
