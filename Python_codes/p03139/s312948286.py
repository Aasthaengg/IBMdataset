N, A, B = map(int,input().split())
if A + B <= N :
    print(str(min(A, B)) + " 0")
else :
    print(str(min(A, B)) + " " + str(abs(N - (2 * N - A - B))))
