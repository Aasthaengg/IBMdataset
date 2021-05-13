N = int(input())
s = input().strip()
t = input().strip()
for i in range(N+1):
    if s[i:N]==t[0:N-i]:
        x = s+t[N-i:N]
        print(len(x))
        break