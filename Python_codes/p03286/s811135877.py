N = int(input())
ans = ""

while N:
    ans = str(N % 2)+ans
    N = -(N//2)

print(ans if ans != ""else 0)
