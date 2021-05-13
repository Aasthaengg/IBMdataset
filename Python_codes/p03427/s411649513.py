N = input()
NN = N
if len(N) == 1:
    print(N)
    exit()
for i in range(1,len(N)):
    if N[i] != '9':
        NN = str(int(N[0])-1)+'9'*len(N[1:])
        break
ans = 0
for nn in NN:
    ans += int(nn)
print(ans)