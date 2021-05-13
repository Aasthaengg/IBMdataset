import sys

s=list(input())
t=list(input())


start=[-1]*26
end=[-1]*26

for i in range(len(s)):
    a=ord(s[i])-ord('a')
    b=ord(t[i])-ord('a')
    if(start[a]!=-1 or end[b]!=-1):
        if(start[a]!=b or end[b]!=a):
            print("No")
            sys.exit()
    start[a]=b
    end[b]=a
print("Yes")