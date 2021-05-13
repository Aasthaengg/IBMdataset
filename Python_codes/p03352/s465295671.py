X = int(input())
print(max(set(b**p for b in range(1,100) for p in range(2,10) if b**p<=X)))