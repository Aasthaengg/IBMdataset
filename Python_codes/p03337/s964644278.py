
def resolve():
    (A,B)=(int(i) for i in input().split())
    print(max([A-B,A+B,A*B]))



if __name__ == "__main__":
    resolve()