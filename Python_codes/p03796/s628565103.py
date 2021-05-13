## B - Training Camp
N = int(input())
val = 1
for n in range(1,N+1):
    val = (val * n) % (10 ** 9 + 7)
print(val)