# -*- coding: utf-8 -*-


k, s = map(int, input().split())

ans = 0

if s == 3*k:
    ans = 1
elif s > 3*k:
    ans = 0
elif s == k:
    ans = int((k + 1) * (k + 2) / 2)
else:
    l = k
    
    while l >= 0:
        t_sum = s - l
        m = s - t_sum
        
        if t_sum > 2*k:
            break
        
        if m < k:
            m = k
            
        while m >= 0:
            n = s - l - m
            
            if n > k:
                break
            
            if n >= 0:
                ans += 1

            m -= 1
        l -= 1

print(ans)
