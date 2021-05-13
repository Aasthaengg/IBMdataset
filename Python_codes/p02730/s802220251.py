S = input().strip()
N = len(S)
flag = 0
if S==S[::-1]:
    x = S[:N//2]
    if x==x[::-1]:
        flag = 1
if flag==1:
    print("Yes")
else:
    print("No")