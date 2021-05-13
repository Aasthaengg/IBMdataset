n = int(input())
li = sorted([int(input()) for i in range(n)])
print(sum(li) - li[-1]//2)