N = int(input())
s = input().strip()
t = input().strip()
flag = 0
for k in range(N,0,-1):
    if s[N-k:]==t[:k]:
        flag = k
        break
print(2*N-flag)