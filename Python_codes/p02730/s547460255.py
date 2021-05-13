S = str(input())

flag = True
N = len(S)

for i in range(N // 2):
    if S[i] != S[-1 * i-1]:
        #print(i,-1*i,S[i],S[-1 * i-1])
        flag = False

for i in range((N-1)//2-1):
    if S[i] != S[(N-1)//2-1-i]:
        #print(i, (N-1)//2-1-i, S[i], S[(N-1)//2-1-i])
        flag = False

for i in range((N+3)//2,N-1):
    if S[i] != S[-1 * i-1]:
        #print(i, (N-1)//2-1-i, S[i], S[(N-1)//2-1-i])
        flag = False

if flag:
    print("Yes")
else:
    print("No")