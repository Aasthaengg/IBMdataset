N = int(input())


def sum(n):
    return n*(n+1)//2


# for i in range(1, N+1):
#     if i % 3 != 0 and i % 5 != 0:
#         ans += i
ans = sum(N)-sum(N//3)*3-sum(N//5)*5+sum(N//15)*15
print(ans)
