A, B = map(int, input().split())
print(len([1 for i in range(A,B+1) if str(i)[0:]==str(i)[::-1]]))