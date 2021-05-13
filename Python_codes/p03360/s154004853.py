a, b, c = map(int, input().split())
k = int(input())
list = [a, b, c]
max = max(list)
if a == max:
    print(b+c+a*2**k)
elif b == max:
    print(a+c+b*2**k)
else:
    print(a+b+c*2**k)