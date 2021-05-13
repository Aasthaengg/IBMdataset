


N = int(input())

if N == 1 or N == 2:
    print(0)
    exit()


ans = 0

i = 2
while i * i <= N:
    if N % i == 0:
        q = N // i
        if q-1 >= 2 and N % (q-1) == i:

            ans += q-1
    i += 1

ans += N-1
print(ans)