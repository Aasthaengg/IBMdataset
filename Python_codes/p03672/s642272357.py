S = input()
for i in range(len(S)):
    S = S[0:-2]
    if len(S)%2==0 and S[0:len(S)//2] == S[len(S)//2:]:
            print(len(S))
            break
