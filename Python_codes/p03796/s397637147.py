N = int(input())
val = 1
for i in range(1, N+1):
    val *= i
    if val > 10**9 + 7:
        val = val%(10**9 + 7)
print(val)