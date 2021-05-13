N, A, B = map(int, input().split())

plan_A = A * N
plan_B = B

if plan_A < plan_B:
    print(str(plan_A))
else:
    print(str(plan_B))
