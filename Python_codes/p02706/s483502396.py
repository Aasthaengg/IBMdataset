N, M = map(int, input().split())

hw_list = map(int, input().split())
for hw in hw_list:
    N -= hw

if N >= 0:
    print(N)
elif N < 0:
    print(-1)