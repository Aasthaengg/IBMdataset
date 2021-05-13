# C - Successive Subtraction

N = int(input())
A = list(int(a) for a in input().split())

M = []
P = []
for a in A:
    if a >= 0:
        P.append(a)
    else:
        M.append(a)

P.sort(reverse=True)
M.sort()
lenP = len(P)
lenM = len(M)    

ans = []
anssum = 0

if lenM ==0:
    if lenP >= 3:
        ans.append((P[-1], P[-2]))
        tmp = P.pop() - P.pop()
        M.append(tmp)
        lenP -= 2
    else:
        ans.append((P[-2], P[-1]))
        tmp = P.pop() - P.pop()
        tmp *= -1
        P.append(tmp)
        lenP -= 2
elif lenP ==0:
    ans.append((M[-1], M[-2]))
    tmp = M.pop() - M.pop()
    P.append(tmp)
    lenP += 1
for i in range(lenP-1):
    ans.append((M[-1], P[-1]))
    tmp = M.pop() - P.pop()
    M.append(tmp)
while M != []:
    ans.append((P[-1], M[-1]))
    tmp = P.pop() - M.pop()
    P.append(tmp)
anssum = P.pop()

print(anssum)
for i in range(len(ans)):
    print(' '.join(map(str, ans[i])))
