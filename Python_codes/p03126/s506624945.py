def resolve():
    N, M = list(map(int, input().split(" ")))
    loved = [0 for _ in range(M)]
    for i in range(N):
        _, *a = list(map(int, input().split(" ")))
        for food in a:
            loved[food-1] += 1
    print(len(list(filter(lambda x: x == N, loved))))
    

if '__main__' == __name__:
    resolve()