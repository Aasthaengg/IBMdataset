n,k = map(int,input().split())
health = list(map(int,input().split()))
s_health = sorted(health)
if n <= k:
    print(0)
    exit()

print(sum(s_health[:n-k]))