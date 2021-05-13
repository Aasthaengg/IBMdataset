N=int(input())
s=input()
t=input()
for i in range(N):
  A=s[i:]
  B=t[:N-i]
  if A==B:
    print(2*N-(N-i))
    exit()
print(2*N)