import fractions

N = int(input())
times = [int(input()) for i in range(N)]

gcdd = 1

for i in range(N):
    num = times[i]
    gcdd = gcdd * num // (fractions.gcd(gcdd, num))


print(gcdd)