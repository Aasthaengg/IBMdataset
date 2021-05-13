N=int(input())
cnt = 0
S=[]
for i in range(N):
    si= input()
    S.append(si)

print(len(list(set(S))))
