a, b = map(int, input().split())
print("Yay!") if abs(a-b) < min(a,b) else print(":(")