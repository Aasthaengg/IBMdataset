A = [int(x) for x in input().split()]
if sum(A) % 2 == max(A) % 2:
    ans = (max(A) * 3 - sum(A)) // 2
else:
    ans = ((max(A) + 1) * 3 - sum(A)) // 2
print(ans)