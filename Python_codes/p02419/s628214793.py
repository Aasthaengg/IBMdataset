n=raw_input().lower()
ans=e=0
while 1:
    if e:break
    for w in raw_input().split():
        if w.lower()==n:ans+=1
        if 'END_OF_TEXT'==w:
            e=1
            break
print ans