input()
a=list(map(int,input().split()))
c=0
for x in a:c+=x%2
print("YES"if c%2==0 else "NO")