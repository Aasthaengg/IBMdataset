A, B = map(int, input().split())
ans = 'Yay!' if max(A, B) <= 8 else ':('
print(ans)
