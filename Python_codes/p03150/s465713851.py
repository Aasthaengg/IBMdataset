s=input()
l='keyence'
n=len(s)
for i in range(n-1):
    for j in range(i,n):
        r=s[:i]+s[j:]
        if(r==l):
            print("YES")
            exit()
print("NO")
