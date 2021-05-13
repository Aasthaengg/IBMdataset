N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
H_temp = [None] * len(H)

for i in range(len(H)):
    H_temp[i] = (abs((T - 0.006 * H[i]) - A), i+1)

H_temp.sort()
print(int(H_temp[0][1]))