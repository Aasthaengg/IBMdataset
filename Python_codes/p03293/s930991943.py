S = list(input().strip())
T = list(input().strip())
flag = 0
for i in range(len(S)):
    S1 = S[i:]+S[:i]
    if S1==T:
        flag = 1
        break
if flag==1:
    print("Yes")
else:
    print("No")