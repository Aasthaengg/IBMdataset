input()
l = list(map(int, input().split()))
print(["No", "Yes"][max(l) < sum(l) - max(l)])