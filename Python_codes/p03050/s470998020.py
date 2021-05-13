N = int(input())

ans = 0

now = 1

while now ** 2 <= N:

    if N % now == 0 and (N // now - 1) > 0 and N // (N // now - 1) == N % (N // now - 1):

        ans += N // now - 1

    now += 1

print (ans)
