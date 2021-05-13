A,B,C = map(int,input().split())
for i in range(300000):
    if A*i % B == C:
        print("YES")
        exit()
print("NO")