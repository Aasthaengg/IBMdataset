N=int(input())
s=str(input())
t=str(input())

if s==t:
    print(len(s))
    exit()

for i in range(1,N+1):
    ans = s + t[-i:]
    if ans[-N:] == t:
        break
print(len(ans))
