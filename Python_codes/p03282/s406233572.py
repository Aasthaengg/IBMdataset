S=input()
K=int(input())

for s_idx,s in enumerate(S):
    s=int(s)
    if s!=1:
        print(s)
        break
    elif s_idx + 1 == K:
        print(s)
        break