N = int(input())
d = list(map(int,input().split()))
d_sorted = sorted(d, reverse = False)

count = d_sorted[(N-1) //2 + 1] - d_sorted[(N-1) // 2]
print(count)