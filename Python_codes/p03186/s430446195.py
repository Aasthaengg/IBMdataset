A,B,C = list(map(int, input().split()))
print(B+C if A+B+1 >= C else A+2*B+1)
