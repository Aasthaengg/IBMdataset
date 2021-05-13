#Two Rectangles
def ABC_52_A():
    A,B,C,D = map(int, input().split())

    if A*B >= C*D:
        print(int(A*B))
    else:
        print(int(C*D))

if __name__ == '__main__':

    ABC_52_A()