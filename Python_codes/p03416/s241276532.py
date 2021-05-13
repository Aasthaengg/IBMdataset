A, B = map(int, input().split())

lis = [i for i in range(A, B+1) if str(i)[0] == str(i)[4] and str(i)[1] == str(i)[3]]
print(len(lis))