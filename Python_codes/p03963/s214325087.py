import sys

number = sys.stdin.readline().split(' ')

N = int(number[0])
K = int(number[1])

ans = K * (K-1)**(N-1)

print(ans)
