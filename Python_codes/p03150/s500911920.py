S = input().strip()
N = len(S)
x = "keyence"
n = len(x)
if N<n:
    flag = 0
else:
    flag = 0
    for i in range(7):
        for j in range(1,8):
            if S[:i]+S[-j:]==x:
                flag = 1
                break
        if flag==1:break
if flag==1:
    print("YES")
else:
    print("NO")