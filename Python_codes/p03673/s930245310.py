n = int(input())
*a, = map(int, input().split())
ans = a[::2][::-1] + a[1::2]
if n%2==0:
    ans = ans[::-1]
print(*ans)