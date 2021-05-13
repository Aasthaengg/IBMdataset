ans = ["GREATER", "LESS", "EQUAL"]
A = int(input())
B = int(input())
if A > B:
    print(ans[0])
elif A == B:
    print(ans[2])
else:
    print(ans[1])