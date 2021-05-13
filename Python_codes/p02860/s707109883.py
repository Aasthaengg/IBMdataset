n=int(input())
s=input()
if n%2==1:
    print("No")
    exit()
a=n//2
for i in range(a):
    if s[i]!=s[a+i]:
        print("No")
        exit()
print("Yes")