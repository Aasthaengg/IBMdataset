
def resolve():
    x, y = list(map(int, input().split()))
    groups = [[1, 3, 5, 7, 8, 10, 12],
              [4, 6, 9, 11],
              [2]]
    for group in groups:
        if x in group and y in group:
            print("Yes")
            return
    print("No")
    


if '__main__' == __name__:
    resolve()