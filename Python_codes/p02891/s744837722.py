import sys
input = sys.stdin.readline

SS = input().rstrip()
ls = len(SS)
Ki = int(input())
lis= []

for K in range(1,4):
    S = list(SS*K)
    N = len(S)
    cnt = 0
    for i in range(1,N-1):
        if S[i-1] == S[i] == S[i+1]:
            S[i] = '5'
            cnt += 1
    for i in range(N-1):
        if S[i]==S[i+1]:
            S[i] = '5'
            cnt += 1
    lis.append(cnt)    
a = lis[0]
d1 = lis[1]-lis[0]
d2 = lis[2]-lis[1]

print(a + d1 *(Ki//2) + d2*((Ki-1)//2))
