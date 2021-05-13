N = int(input())
s = input()
t = input()
ans = N*2
tmp = 0
for i in range(N):
    if(s[N-i-1:N] == t[0:i+1]):
        tmp = i + 1
print(ans-tmp)