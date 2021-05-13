
N = int(input())
a = list(map(int, input().split()))

X = [0] * (N // 2) + a[N//2:]
#print(X)

for i in range(N//2):
    idx = -(i + N//2 + 1 + N % 2)
    step = N + idx + 1
    #print(idx, step)
    #print(X[idx:N+1:step])
    X[idx] = X[idx] if sum(X[idx:N+1:step]) % 2 == a[idx] else 1 - X[idx]

#print(X)

count = 0
s = ""
for i in range(N):
    if X[i] == 1:
        count += 1
        s += str(i+1) + " "

print(count)
print(s)