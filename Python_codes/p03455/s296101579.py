a, b= list(map(int, input().split()))
c = a*b
d = c %2
ans = 0
if d == 0 :
    print("Even")
else:
    print("Odd")