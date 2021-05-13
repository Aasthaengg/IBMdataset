a, b, c = list(map(int, input().split()))
# x2, y2, x3, y3 = list(map(int, input().split()))
# x = list(map(int, input().split()))
# abc = [int(input()) for i in range(5)]
# n = int(input())
# n, m = list(map(int, input().split()))
if a+b >= c-1:
    print(b+c)
else:
    print(b+(a+b+1))
