n=int(input())
s=input()
k=0
if n%2==1:
    print('No')
else:
    for i in range(len(s)//2):
        if s[i]==s[i+len(s)//2]:
            k=1
        else:
            print('No')
            exit()
if k== 1:
    print('Yes')