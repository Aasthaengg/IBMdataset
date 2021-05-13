N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

buff = []

for i in range(N):
    buff.append(sum(A[:i+1]) + sum(B[i:]))

print(max(buff))