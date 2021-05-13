H, N = map(int, input().split())
A = list(map(int, input().split()))

rest_H = H - sum(A)

if rest_H <= 0:
    print("Yes")
else:
    print("No") 