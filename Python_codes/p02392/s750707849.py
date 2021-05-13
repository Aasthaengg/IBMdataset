pred = lambda a: all(a[i] < a[i+1] for i in range(len(a)-1))

a = list(map(int, input().split()))

print("Yes" if pred(a) else "No")