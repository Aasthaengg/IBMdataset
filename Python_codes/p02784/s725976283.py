H, N = map(int, input().split())
A = sorted(map(int, input().split()))
print("Yes" if(sum(A) >= H) else "No")
