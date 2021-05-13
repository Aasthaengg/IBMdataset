s=list(input())
N=len(s)
K=int(input())
num=123

for i in range(N):
    diff=(num-ord(s[i]))%26
    if K==0:
        break
    if diff<=K:
        s[i]="a"
        K=K-diff
#print(s)
#print(K)
if K>0:
    K=K%26
    s[N-1]=chr(ord(s[N-1])+K)
#print(s)
print("".join(s))
