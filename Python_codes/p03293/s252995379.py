S = input()
T = input()
for i in range(len(S) + 1):
    tmp = S[-1:]
    S = tmp + S[0:len(S)-1]
    if(S == T):
        print("Yes")
        exit()
print("No")