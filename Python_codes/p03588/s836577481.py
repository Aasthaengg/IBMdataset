N = int(input())
ab = {}
for _ in range(N):
    a, b = map(int, input().split())
    ab[a] = b
    
print(max(ab)+ab[max(ab)])