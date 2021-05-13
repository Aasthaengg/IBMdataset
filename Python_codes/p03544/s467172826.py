N = int(input())
r = [2,1]
for _ in range(N-1):r.append(r[-1]+r[-2])
print(r[-1])