n = int(input())
b = list(map(int, input().split()))

ans = [0] * n
for i in range(1,n+1):
    num = -1
    for j in range(n+1-i):
        if(b[j] == j+1):
            num = j
    if(num == -1):
        print(-1)
        exit()
    ans[-i] = num + 1
    del b[num]

print('\n'.join(map(str, ans)))