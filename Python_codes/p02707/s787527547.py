N = int(input())
A = list(map(int, input().split()))
B = [0]*(N+1)
for i in A:
    B[i] += 1
print('\n'.join(list(map(str, B[1:]))))