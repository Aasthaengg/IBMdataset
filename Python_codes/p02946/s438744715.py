K, X = map(int, input().split())
a = [X]
if K == 1 :
    print(*a)
    exit()

for i in range(1,K):
    a.append(X-i)
    a.append(X+i)

print(*(sorted(a)))