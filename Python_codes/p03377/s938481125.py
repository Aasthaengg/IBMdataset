A,B,X = map(int,input().split())
ans = X-A
if (ans<=B)&(ans>=0):
    print("YES")
else:
    print("NO")