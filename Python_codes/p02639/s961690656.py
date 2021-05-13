A = list(map(int, input().split()))

key = 0
for i,a in enumerate(A):
    if a == 0:
        key = i+1
        break
print(key)
