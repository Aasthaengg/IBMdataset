a,b,c = (int(i) for i in input().split())
ans = False
if a == b and b==c:
    ans = True
if ans:
    print("Yes")
else:
    print("No")