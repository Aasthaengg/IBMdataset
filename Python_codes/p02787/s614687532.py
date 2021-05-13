HP, n_magic = map(int,input().split())
attack_ls, power_taken_ls = [0]*(n_magic+1), [0]*(n_magic+1)
for i in range(n_magic):
    attack_ls[i+1], power_taken_ls[i+1] = map(int,input().split())
max_attack = HP + max(attack_ls)
dp = [[float('inf')]*(max_attack+1) for _ in range(n_magic+1)]
dp[0][0] = 0
for i in range(1,n_magic+1):
    for attack in range(max_attack+1):
        if attack - attack_ls[i] >= 0:
            dp[i][attack] = min(dp[i][attack], dp[i][attack-attack_ls[i]] + power_taken_ls[i])
        dp[i][attack] = min(dp[i-1][attack], dp[i][attack])
ans = float('inf')
for attack in range(HP, max_attack+1):
    ans = min(dp[n_magic][attack], ans)
print(ans)
        
