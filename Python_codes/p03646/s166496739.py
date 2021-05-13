K = int(input())
N = 50
moku = N-1 + K//N
t = K%N

ans = [moku-t for i in range(N)]
for i in range(t):
    ans[i]=moku+N-t

print(N)
print(" ".join(list(map(str,ans))))