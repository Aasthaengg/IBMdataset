from operator import itemgetter

N = int(input())
C = []
for i in range(N):
    C.append(list(map(int, input().split())))

C.sort(key=itemgetter(1))

elapsed = 0
for i in range(N):
    elapsed += C[i][0]
    if elapsed > C[i][1] :
        print("No")
        exit(0)

print("Yes")
