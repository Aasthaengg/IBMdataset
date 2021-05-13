N = int(input())
S = []
for _ in range(N):
    S.append(int(input()))

for num in S:
    if num%2!=0:
        print("first")
        exit()
print("second")