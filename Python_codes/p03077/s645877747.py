n = int(input())
li = [int(input()) for _ in range(5)]

mn = min(li)
groups = (n + mn - 1) // mn
ans = 5 + groups - 1
print(ans)
