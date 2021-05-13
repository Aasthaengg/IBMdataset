N = int(input())

def sum_number_line(a: int, n: int) -> int:
    return (2*a + (n - 1)*a) * n // 2

ans = 0
for i in range(1, N + 1):
    ans += sum_number_line(i, N//i)

print(ans)