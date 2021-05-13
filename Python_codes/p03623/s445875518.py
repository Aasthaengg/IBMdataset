x,a,b = map(int, input().split())

print("A" if min(abs(x-a), abs(x-b))==abs(x-a) else "B")