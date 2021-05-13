N = int(input())
s = input()
t = input()
d = 0
for i in range(1,N+1):
    if t.startswith(s[i-1:]):
        d = N - i + 1
        break
print(2*N - d)
