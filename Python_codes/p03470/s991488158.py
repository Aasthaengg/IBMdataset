N = int(input())
lin = [int(input()) for i in range(N)]
print(len(sorted(list(set(lin)))))