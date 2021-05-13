A, B, K = map(int, input().split())
ans = 0
curr = min(A, B)
while K > 0:
    if A % curr == 0 and B % curr == 0:
        K -= 1
        ans = curr
    curr -= 1
print(ans)