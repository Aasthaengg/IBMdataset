#2019/10/10
A, B = map(int, open(0).read().split())
print(A+B if B%A==0 else B-A)