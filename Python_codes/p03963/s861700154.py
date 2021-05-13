n,k = [int(x) for x in input().split()]

ans = k * (k - 1)**(n - 1)
print(ans)