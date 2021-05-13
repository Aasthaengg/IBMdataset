
n = int(input())

ans = 0

for i in range(n):
    l, r = [int(i) for i in input().split()]
    ans += abs(l-r) +1
    
print(int(ans))