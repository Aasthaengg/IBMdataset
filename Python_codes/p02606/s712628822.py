l, r, x = map(int, input().split(' '))

ans = r // x - (l-1) // x
print(ans)