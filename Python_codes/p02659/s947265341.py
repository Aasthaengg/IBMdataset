def resolve():
    IN = input().split()
    A = int(IN[0])
    B = int(IN[1].replace(".", ""))
    print((int(A)*int(B))//100)

if '__main__' == __name__:
    resolve()