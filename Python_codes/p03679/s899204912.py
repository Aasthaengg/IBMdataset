x, a, b = map(int, input().split())
ans = "delicious" if b <= a else "dangerous" if b > a+x else "safe"
print(ans)