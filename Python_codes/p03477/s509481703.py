w = list(map(int, input().split()))
if sum(w[:2])>sum(w[:-3:-1]):
    print("Left")
elif sum(w[:2])==sum(w[:-3:-1]):
    print("Balanced")
else:
    print("Right")
