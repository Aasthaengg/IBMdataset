A = int(input())
B = int(input())
ans = {1,2,3}
ans.discard(A)
ans.discard(B)
print(*ans)
