n = int(input())
a_L = list(map(int,input().split()))

a_L = sorted(a_L)

print(abs(a_L[0]-a_L[-1]))