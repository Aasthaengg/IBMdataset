N=int(input())
s=input()
t=input()
chohuku=0
for i in range(N):
  if s[i:]==t[:N-i]:
    chohuku=len(s[i:])
    break
print(N+N-chohuku)