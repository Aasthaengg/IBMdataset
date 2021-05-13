O = list(input())
E = list(input())
ans = []

if len(O) == len(E):
    for i in range(len(O)):
        ans.append(O[i])
        ans.append(E[i])
else:
    for i in range(len(O)-1):
        ans.append(O[i])
        ans.append(E[i])
    ans.append(O[-1])
    
print("".join(ans))

