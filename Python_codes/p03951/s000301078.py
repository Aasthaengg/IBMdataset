N = int(input())
s = input()
t = input()

ans = N*2
for n in range(N):
    if s[n:] == t[:N-n]:
        ans -= len(s[n:])
        break
        
print(ans)