*ABC, = map(int, input().split())
K = int(input())

biggest = ABC.index(max(ABC))
ans = sum(ABC) - ABC[biggest] + ABC[biggest] * 2 ** K

print(ans)
