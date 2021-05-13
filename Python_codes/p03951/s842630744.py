N=int(input())
s=list(input())
t=list(input())
f=s+t
if s==t:
    print(len(s))
    exit()
for i in range(0,N):
    if s[-i:]==t[:i]:
        f=s+t[i:]
print(len(f))