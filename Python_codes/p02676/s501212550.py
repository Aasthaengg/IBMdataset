K = int(input())
S = input()
if len(S)<=K:
    print(S)
else:
    s_list = list(S)[0:K]
    print("".join(s_list)+"...")