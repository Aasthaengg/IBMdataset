N = int(input())
H = list(map(int, input().split()))
r_H = list(reversed(H))

for i in range(N-1):
    if r_H[i+1] - r_H[i] > 1:
        print("No")
        exit()
    if r_H[i+1] - r_H[i] == 1:
        r_H[i+1] = r_H[i+1] - 1
print("Yes")