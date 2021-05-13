# 170 B
X , Y = list(map(int, input().split()))
ans = 0
for i in range(0, X+1):
    if (X-i)*2 + i*4 == Y:
        ans = 1
        
print('Yes') if ans == 1 else print('No')