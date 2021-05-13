N = int(input())
s = input()
t = input()
for i in range(N, -1, -1):
    if s.endswith(t[:i]):
        print(N+len(t)-i)
        exit()
