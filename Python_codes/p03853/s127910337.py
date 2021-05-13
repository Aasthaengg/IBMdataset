H, W = map(int, input().split())
arr = [input() for _ in range(H)]
ans = [arr[i//2] for i in range(2*H)]
print("\n".join(ans))