N = int(input())
i = []
for j in range(N):
    i.append(int(input()))
i.sort(reverse=True)
i[0] = i[0]//2
print(sum(i))