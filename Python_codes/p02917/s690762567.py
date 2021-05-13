N = int(input())
b = [int(x) for x in input().split()]
val = b[0]
val += b[-1]
for i in range(N-2):
    val += min(b[i], b[i+1])
print(val)
