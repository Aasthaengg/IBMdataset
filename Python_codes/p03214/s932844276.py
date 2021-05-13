N = int(input())
A = list(map(int, input().split()))

avg = sum(A) / N

diff = [[abs(val - avg), itr] for itr, val in enumerate(A)]

sdiff = sorted(diff, key=lambda x: (x[0],x[1]))

print(sdiff[0][1])