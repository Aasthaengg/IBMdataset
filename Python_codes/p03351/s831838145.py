a,b,c,d = map(int, input().split())
ans = [c-a,c-b,b-a]
for i in range(len(ans)):
    if ans[i]<0:
        ans[i]=ans[i]*-1
if ans[0]<=d or ans[1]<=d and ans[2]<=d:
    print("Yes")
else:
    print("No")
