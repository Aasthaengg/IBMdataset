N = int(input())
s = input()
t = input()
k = 0
for i in range(N+1):
    if s[-i:] == t[:i]:
        k = i
print(2*N-k)
