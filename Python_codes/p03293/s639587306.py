S=input()
T=input()

S_new=S

ans="No"

for i in range(len(S)):
    S_new = S_new[-1]+S_new[:-1]
    if S_new == T:
        ans="Yes"
        break
    else:
        continue
print(ans)
