n = int(input())
m = input().split()
arr = []
for i in range(n):
    arr.append(int(m[i]))
arr.reverse()
print(' '.join(map(str, arr)))