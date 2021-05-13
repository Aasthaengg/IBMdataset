n, m, x = map(int, input().split())
gate = list(map(int, input().split()))

left_gates = [i for i in gate if i < x]
right_gates = [j for j in gate if x < j]

ans = min(len(left_gates), len(right_gates))

print(ans)