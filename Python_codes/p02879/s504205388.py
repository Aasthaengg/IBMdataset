A, B = map(int,input(). split())

answer = A * B

if A >= 10 or B >= 10:
    print("-1")
else:
    print(answer)