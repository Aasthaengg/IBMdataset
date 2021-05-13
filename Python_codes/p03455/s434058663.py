a,b = map(int,input().split())

answer = a * b

if a*b / 2 == a*b // 2:
    print("Even")
else:
    print("Odd")
