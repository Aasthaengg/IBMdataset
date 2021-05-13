N, blue, red = map(int, input().split())

ans = N // (blue + red) * blue
rem = N % (blue + red)
ans += min(rem, blue)
print(ans)