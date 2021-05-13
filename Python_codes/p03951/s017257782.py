n=int(input())
s=input();t=input()
a=0
if s == t:
    print(n)
    exit()
for i in range(1,n+1):
    if s[0:i] == t[-i:]:
        a=i
b = 0
for i in range(1,n+1):
    if s[-i:] == t[0:i]:
        b=i
a = max(a,b)
print(n*2-a)