N = int(input())

# t = []
# for i in range(1, N+1):
#     if N // i == N % i:
#         print("→ :", i)
#         t.append(i)
#     else:
#         print("  :", i)

# print("G:", sum(t))

ans = (N-1) if N != 2 else 0
cur = 2
while (N-cur)//cur >= cur:

    if (N-cur)%cur == 0:
        a = (N-cur)//cur
        if N%a!=0:
            ans += (N-cur)//cur
    cur += 1

print(ans)