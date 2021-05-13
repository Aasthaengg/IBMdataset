N = int(input())

div = []
i = 1

while i * i < N:
    if N % i == 0:
        div.append(N // i)
    i += 1

ans = 0  
for i in div:
    if N // (i - 1)== N % (i - 1):
        ans += i - 1
print(ans)