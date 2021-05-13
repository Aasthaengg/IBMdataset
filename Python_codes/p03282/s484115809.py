s=input()
k=int(input())
n=len(s)
for i in range(min(n,k)):
    if s[i]!="1":
        print(s[i])
        exit()
print(1)
