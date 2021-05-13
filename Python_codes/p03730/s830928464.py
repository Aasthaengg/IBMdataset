A, B, C = map(int, input().split())

for i in range(1, B+1):
    Z = (A * i) % B
    if Z == C:
        print("YES")
        exit()
print("NO")
