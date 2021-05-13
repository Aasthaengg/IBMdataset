N = int(input())
A = map(int, input().split())
l = [abs(N - (n * 2 + 1)) for n in range(N)]

if sorted(A) == sorted(l):
    print(pow(2, N//2) % (pow(10,9) + 7))
else:
    print(0)