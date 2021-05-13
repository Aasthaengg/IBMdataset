N=int(input())
s=input()
t=input()
u=s+t
for i in range(N):
    if s[i:N]==t[0:N-i]:
        u=s+t[N-i:N]
        break
print(len(u))