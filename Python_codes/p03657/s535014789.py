#2019/10/10
A, B = map(int, open(0).read().split())
print("Possible" if A%3==0 or B%3==0 or (A+B)%3==0 else "Impossible")