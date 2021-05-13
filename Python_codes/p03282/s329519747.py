S=input()
K=int(input())
for n in range(min(len(S),K)):
    if S[n]!="1":
        print(S[n])
        break
else:
    print(1)