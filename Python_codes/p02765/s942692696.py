def resolve():
    N, R = list(map(int, input().split()))
    print(R if N >= 10 else R+100*(10-N))

if '__main__' == __name__:
    resolve()