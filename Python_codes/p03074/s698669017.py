N,K = map(int,input().split())
S = input()
l = [1]
for i in range(N-1):
    if S[i] == S[i+1]:
        l[-1] += 1
    else:
        l.append(1)
if S[0] == "0":
    l = [0] + l
if S[-1] == "0":
    l += [0]
s = [0]
for i in range(len(l)):
    s.append(s[-1]+l[i])
if len(l) <= 2*K + 1:
    print(s[-1])
else:
    cnt = 0
    for i in range((len(l)-2*K-1)//2+1):
        cnt = max(cnt,s[2*K+2*i+1]-s[2*i])
    print(cnt)