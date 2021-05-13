N = int(input())
D = list(map(int,input().split()))

sorted_D = sorted(D)

f = N//2 - 1
s = f + 1

print(sorted_D[s]-sorted_D[f])