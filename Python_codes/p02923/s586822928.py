N = int(input())
H = list(map(int,input().split()))

count = [0]

for i in range(1,N):
    if H[i-1] >= H [i]:
        count.append(count[-1] + 1)
    else:
        count.append(0)

print(max(count))