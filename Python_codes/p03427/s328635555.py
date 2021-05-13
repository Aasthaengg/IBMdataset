N = int(input())

N2 =str(N)[0]+(len(str(N))-1)*"9"
ans = 0
for n in N2:
    ans+=int(n)
if int(N2) > N:
    ans-=1
print(ans)