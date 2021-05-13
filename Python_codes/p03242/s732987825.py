n=list(input())
p=""
for i in range(3):
    if n[i]=="1":
        n[i]="9"
    else:
        n[i]="1"
for i in range(3):
    p+=n[i]
print(p)