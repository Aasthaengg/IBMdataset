n,k=map(int, input().split())
s=input()
for i in range(len(s)):
    if i+1==k:
        print(chr(ord(s[i])+32),end='')
    else:
        print(s[i],end='')
