[n, m] = map(int, input().split())
answer = 0
if m//2 <= n:
    answer = m//2
else:
    answer = n
    m -= 2*n
    answer += m//4

print(answer)