A, B = map(int, input().split())
print("Possible" if any((i%3==0 for i in (A, B, A+B))) else "Impossible")