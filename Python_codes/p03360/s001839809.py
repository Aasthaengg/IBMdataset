ABC = list(map(int, input().split()))
K = int(input())
ABC.sort()
for i in range(K):
    ABC[2] *= 2
print(sum(ABC))
