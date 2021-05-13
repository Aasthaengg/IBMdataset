N = int(input())
s = input()
t = input()

for i in range(N, 0, -1):
    if s[-i:] == t[:i]:
        print(N * 2 - i)
        exit()
print(2 * N)