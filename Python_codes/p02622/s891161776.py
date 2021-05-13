S=input()
T=input()

ans = 0

for c1,c2 in zip(S,T):
    if c1 != c2:
        ans +=1

print(ans)