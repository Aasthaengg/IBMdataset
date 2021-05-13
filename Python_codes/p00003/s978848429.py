count=int(raw_input())
ans =[]
for i in range(0,count):
    a,b,c=map(int,raw_input().split())
    if pow(a,2)+pow(b,2)==pow(c,2):
        ans.append("YES")
    elif pow(a,2)+pow(c,2)==pow(b,2):
        ans.append("YES")
    elif pow(b,2)+pow(c,2)==pow(a,2):
        ans.append("YES")
    else:
        ans.append("NO")

for i in range(0,count):
    print ans[i]