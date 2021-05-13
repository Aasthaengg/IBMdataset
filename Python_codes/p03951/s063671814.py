N = int(input())
s = input().strip()
t = input().strip()
k = 0
for i in range(1,N+1):
    if s[-i:]==t[:i]:
        k = i
        continue
print(2*N-k)