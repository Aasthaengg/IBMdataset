A, B = map(int, input().split())
ans = int((A+B)/2) if (A+B) % 2 == 0 else "IMPOSSIBLE"
print(ans)