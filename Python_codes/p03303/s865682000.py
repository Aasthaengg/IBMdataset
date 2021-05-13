s=input()
w=int(input())
a=""
for i in range(0,len(s)):
    if i%w==0:
        a=a+s[i]
print(a)