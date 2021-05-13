S = input()
K = int(input())
c = 0
f = 1
for i in range(len(S)):
    if S[i] == '1':
        c+=1
    else:
        f = S[i]
        break
if K<=c: print(1)
else: print(f)
