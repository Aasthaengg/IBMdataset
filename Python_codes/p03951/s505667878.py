
N = int(input())
s = input()
t = input()

ans=0
for i in range(N):
    if s==t:
        ans=N
        break
    elif s[i:] == t[:-i]:
        ans=N+i
        break
if ans!=0:
    print(ans)
else:
    print(N*2)