s=input()
if len(s)%2==0:
    for i in range(len(s)//2):
        print(s[2*i],end='')
else:
    for i in range(len(s)//2+1):
        print(s[2*i],end='')
print()