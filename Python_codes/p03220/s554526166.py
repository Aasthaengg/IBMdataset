N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = []

for H in H:
    ans.append(abs(T - H * 0.006 - A))
    
print(ans.index(min(ans)) + 1)
