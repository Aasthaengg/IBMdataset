S = input()
T = input()

for _ in range(len(S)):
    S_lst = list(S)
    tmp = S[0]
    for i in range(len(S) - 1):
        S_lst[i] = S_lst[i+1]
    S_lst[-1] = tmp
    S = ''.join(S_lst)
    
    if S == T:
        print("Yes")
        exit()
else:
    print("No")