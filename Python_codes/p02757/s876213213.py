N, P = map(int, input().split())
S = input()

cnt = 0
if P == 2 or P == 5:
    for i in range(N):
        if int(S[i]) % P == 0:
            cnt += (i+1)
            
else:
    dic = dict()
    dic[0] = 1
    r = 0
    for i in range(N):
        s = (pow(10,i,P)*int(S[N-1-i]) + r) % P
        r = s
        if not s in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    for i in dic:
        cnt += dic[i]*(dic[i]-1)/2
        
print(int(cnt))