mini, maxi, K_ban = map(int, input().split())

if (maxi - mini + 1 <= 2 * K_ban):
    ans = [i for i in range(mini, maxi + 1)]

else:
    left = [i for i in range(mini, mini + K_ban)]
    right = [i for i in range(maxi - K_ban + 1, maxi + 1)]
    
    ans = left + right
    

[print(n) for n in ans]