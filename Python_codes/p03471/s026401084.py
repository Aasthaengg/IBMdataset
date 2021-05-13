N, Y = map(int, input().split())

for man in range(N+1):
    for sen in range(N+1):
        if man + sen > N:
            break
        if 10000*man + 5000*sen + 1000*(N-man-sen) == Y:
            print(man, sen, N-man-sen)
            exit()
print('-1 -1 -1')
