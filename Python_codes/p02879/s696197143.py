#n = int(input())
a, b = map(int, input().split())
#l = list(map(int, input().split()))
#s = input()

ans = 0

if (a < 1 or a > 9) or (b < 1 or b > 9):
    ans = -1
else:
    ans = a * b
print(ans)


