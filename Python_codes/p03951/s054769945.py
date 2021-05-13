N=int(input())
s=input()
t=input()
res = 0
for i in range(N,-1,-1):
    if s[N-i:]==t[:i]:
        res = 2*N-i
        break
if res==0:
    res = 2*N
print(res)