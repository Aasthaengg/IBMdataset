N = int(input())
member = sorted(map(int, input().split()))
ans = sum(member[N::2])
print(ans)
