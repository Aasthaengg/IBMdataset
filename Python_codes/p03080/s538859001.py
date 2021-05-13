N=int(input())
s=input()
R=0;B=0;
for c in s:
    if c=='R':
        R+=1
    if c=='B':
        B+=1
print('Yes' if R>B else 'No')