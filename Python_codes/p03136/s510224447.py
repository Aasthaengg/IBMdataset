n = int(input())
l = list(map(int, input().split()))
longest = max(l)
l.remove(longest)
print("Yes" if longest < sum(l) else "No")