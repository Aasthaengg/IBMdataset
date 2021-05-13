a,b,c=input()
n=[a,b,c]
for i in range(3):
    if n[i]=='1':
        n[i]='9'
    elif n[i]=='9':
        n[i]='1'
for i in n:
    print(i,end = "")