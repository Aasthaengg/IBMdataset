def resolve():
    N = int(input())
    prizes = set()
    for i in range(N):
        prizes.add(input())
    print(len(prizes))

if '__main__' == __name__:
    resolve()