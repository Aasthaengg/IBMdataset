N = int(input())

a = [0] + list(map(int, input().split()))
a = sorted(a)

# print(f"N:{N} a:{a}", file=sys.stderr)
max_power = 0
for i in range(N):
    max_power += a[(N + 1) + 2 * i]
print(max_power)