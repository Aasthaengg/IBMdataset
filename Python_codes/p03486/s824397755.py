s = list(input())
t = list(input())

S = sorted(s)
T = sorted(t, reverse = True)


U = min(len(s), len(t))

for i in range(U):
    if S[i] < T[i]:
        print("Yes")
        exit()
    elif S[i] == T[i]:
        continue
    else:
        print("No")
        exit()
    
if len(S) < len(T):
    print("Yes")
else:
    print("No")