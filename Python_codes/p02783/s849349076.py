h, a = list(map(int, input().split()))
print(h // a + min(h % a, 1))
