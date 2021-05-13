A, B, C = map(int, input().split())

K = int(input())

num = 0
ans = A+B+C
while True:
    num += 1
    ans += max(A,B,C)*(2**(num-1))
    if num == K:
        break

print(ans)