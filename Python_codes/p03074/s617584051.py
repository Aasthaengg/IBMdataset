from sys import stdin
N,K = [int(x) for x in stdin.readline().rstrip().split()]
S = (stdin.readline().rstrip())
zero = []
one = []
tmp = 1
S += "@"

for i in range(N):
    if S[i] == S[i+1]:
        tmp += 1
    else:
        if S[i] == "0":
            zero.append(tmp)
        else:
            one.append(tmp)
        tmp = 1
        
if K >= len(zero):
    print(N)
else:
    if S[0] == "1":
        tmp = sum(zero[:K]) + sum(one[:K+1])
        ans = sum(zero[:K]) + sum(one[:K+1])

        for i in range(0,len(zero)-K):
            tmp -= zero[i]
            tmp += zero[i+K]
            tmp -= one[i]
            if not i+K+1 >= len(one):
                tmp += one[i+K+1]
            ans = max(ans,tmp)
        print(ans)
    else:
        tmp = sum(zero[:K]) + sum(one[:K])
        ans = sum(zero[:K]) + sum(one[:K])

        for i in range(0,len(zero)-K):
            tmp -= zero[i]
            tmp += zero[i+K]
            if i != 0:
                tmp -= one[i-1]
            if not i+K >= len(one):
                tmp += one[i+K]
            ans = max(ans,tmp)
        print(ans)