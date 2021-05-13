input()
if len(["" for i in input().split() if int(i)%2 == 1])%2 == 0:
    print("YES")
else:
    print("NO")