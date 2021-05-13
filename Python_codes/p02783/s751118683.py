H, A = map(int, input().split())
for i in range(H+1):
    if H <= A*i:
        print(i)
        break
