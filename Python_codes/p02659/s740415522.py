def resolve():
    A, B = input().split()
    ans = int(A)*int(B[0])*100+int(A)*int(B[2:])
    print(str(ans)[:-2] if len(str(ans)) >= 3 else "0")
resolve()