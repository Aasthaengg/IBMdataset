S = input()
T = input()
flag = 0
for i in range(1,len(S)+1):
    S = S[-1] + S[:-1]
    if S == T:
        flag = 1
        print("Yes")
        break
    
if flag == 0:
    print("No")