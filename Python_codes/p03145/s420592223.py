def resolve():
    ab, bc, ca = list(map(int, input().split()))
    print(ab*bc//2)
    

if '__main__' == __name__:
    resolve()