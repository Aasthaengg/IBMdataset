N = int(input())
A = sorted(map(int, input().split()))
print("YES" if all(A[i]-A[i-1]>0 for i in range(1, N)) else "NO")