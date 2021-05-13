N = int(input())
A = list(map(int, input().split()))

A_sort = sorted(A, reverse=True)
Alice = [a for i, a in enumerate(A_sort) if i%2==0]
Bob = [a for i, a in enumerate(A_sort) if i%2==1]

ans = sum(Alice) - sum(Bob)

print(ans)