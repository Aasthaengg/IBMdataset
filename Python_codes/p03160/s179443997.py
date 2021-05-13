n = int(input())
scaffolding = input().rstrip().split()
scaffolding = list(map(int, scaffolding))
res=[0 for i in range(n)]
res[1]=abs(scaffolding[1]-scaffolding[0])

for i in range(2,n):
    cost_1 = abs(scaffolding[i]-scaffolding[i-1])
    cost_2 = abs(scaffolding[i]-scaffolding[i-2])
    res[i]= min(res[i-1]+cost_1, res[i-2]+cost_2)

print(res[n-1])