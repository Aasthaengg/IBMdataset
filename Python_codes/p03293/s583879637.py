s=input()
t=input()
for i in range(len(s)+1):
    if s==t:
        print('Yes')
        exit()
    else:
        s=s[1:]+s[0]
print('No')