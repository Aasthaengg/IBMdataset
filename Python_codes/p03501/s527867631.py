N,A,B = [int(x) for x in input().split()]

plan_1 = A*N
plan_2 = B

ans=min(plan_1,plan_2)
print(ans)