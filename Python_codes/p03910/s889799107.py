N = int(input())
def calc(n):
    return (n*(n+1))//2
max_n = 0
for i in range(1, N+1):
    if calc(i) >= N:
        max_n = i
        break
for i in range(1, max_n+1):
    if calc(max_n) - N == i:
        continue
    else:
        print(i)