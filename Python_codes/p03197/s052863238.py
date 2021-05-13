n = int(input())
a = list(int(input())%2 for _ in range(n))
a = list(set(a))
print("second" if a == [0] else "first")