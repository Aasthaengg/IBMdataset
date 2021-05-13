S = input().rstrip()
T = input().rstrip()
flg = False
for i in range(len(S)):
    cnt = 0
    for j, s in enumerate(S):
        if s==T[j-i]: cnt += 1
    if cnt==len(S):
        flg = True
if flg:
    print("Yes")
else:
    print("No")