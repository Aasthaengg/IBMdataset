ver = list(map(int, input().split()))
ver.remove(max(ver))

ans = ver[0] * ver[1] // 2

print(ans)