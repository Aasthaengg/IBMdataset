k, s  = map(int, input().split())

ans1 = 0
ans2 = 0
ans3 = 0

for i in range(k+1):
    for j in range(i, k+1):    
        if 0 <= s-i-j <= k and j <= s-i-j:
            if i == j == s-i-j:
                ans1 +=1
            elif i == s-i-j or i == j or j == s-i-j:
                ans2 += 1
            else:
                ans3 += 1
                    

print(ans1+ans2*3+ans3*6)
#print(ans1, ans2, ans3)
