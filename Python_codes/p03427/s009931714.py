N = [int(i) for i in list(input())][::-1]

if len(N) == 1:
    print(N[0])
    exit()

p = N[-1]
q = sum(N)

ans = 0
for i in range(len(N)-1):
    if N[i] != 9:
        for j in range(i,len(N)):
            if N[j] != 0:
                N[j] -= 1
                N[i] = 9
            else:
                N[j] = 9

N[-1] = p-1
print(max(sum(N),q))
