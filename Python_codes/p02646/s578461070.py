A,V = list(map(int, input().split()))
B,W = list(map(int, input().split()))
T = int(input())
print("YES" if (V-W) * T >= abs(B-A) else "NO")