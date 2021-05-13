S=input()
K=int(input())
if all(S[i]=="1" for i in range(min(K,len(S)))):
    print(1)
else:
    for i in range(min(K,len(S))):
        if S[i]!="1":
            print(int(S[i]))
            break
