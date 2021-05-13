N = int(input())

if N % 2:
    print(0)
    exit()

ans = 0
div = 10
while(div <= N):
    ans += N // div
    div *= 5
print(ans)
