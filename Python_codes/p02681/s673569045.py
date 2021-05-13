S = list(input())
T= list(input())
ans=True
num=len(S)
for i in range(num):
    if S[i]!=T[i]:
        ans=False
if ans:
    print("Yes")
else:
    print("No")