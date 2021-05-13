a, b = map(int, input().split())
if not (a % 3) * (b % 3) * ((a + b) % 3) :
    print("Possible")
else: 
    print("Impossible")