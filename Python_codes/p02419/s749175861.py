w=input().lower()
c=[]
s=input()
while(s!='END_OF_TEXT'):
    c+=s.lower().split();
    s=input()
print(len([x for x in c if x==w]))

