q = int(input())
l, r = [0] * q, [0] * q
for i in range(q):
    l[i], r[i] = map(int, input().split())
 
mini = min(min(l), min(r))
maxi = max(max(l), max(r))
ans = [0] * (maxi + 1)
prime = [0] * (maxi + 1)
def judge_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True if n != 1 else False
 
for i in range((mini + 1) // 2, maxi + 1):
    prime[i] = judge_prime(i)
 
for i in range(mini, maxi + 1, 2):
    ans[i] = ans[i - 2] + 1 if prime[i] and prime[(i + 1) // 2] else ans[i - 2]
for i in range(q):
    print(ans[r[i]] - ans[max(0, l[i] - 2)])