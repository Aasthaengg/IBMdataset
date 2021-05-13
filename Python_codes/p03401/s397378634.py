n = int(input())
ns = [0]
ns += list(map(int, input().split()))
ns.append(0)
total_cost = sum(abs(ns[i]-ns[i+1]) for i in range(n+1))
for i in range(1, n+1):
    print(total_cost-(abs(ns[i-1]-ns[i])+abs(ns[i]-ns[i+1]))+abs(ns[i-1]-ns[i+1]))
