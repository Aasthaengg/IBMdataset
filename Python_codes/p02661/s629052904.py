n = int(input())
a = []
b = []
for i in range(n):
	a_1, b_1 = input().split()
	a.append(int(a_1))
	b.append(int(b_1))
a.sort()
b.sort()
is_odds = n % 2 == 0
a_med = a[(n + 1) // 2 - 1] if not is_odds else (a[n // 2 - 1] + a[n // 2]) / 2
b_med = b[(n + 1) // 2 - 1] if not is_odds else (b[n // 2 - 1] + b[n // 2]) / 2
from_a = a_med if not is_odds else int(a_med * 2)
to_b = b_med if not is_odds else int(b_med * 2)
print(to_b - from_a + 1)