N = int(input())
a_list = [0]+[int(e) for e in input().split()]

ans = 0

for i in range(N):
    if a_list[a_list[i]] == i:
        ans += 1
        
print(ans//2)