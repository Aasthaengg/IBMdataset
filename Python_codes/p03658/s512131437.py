k=int(input().split()[1])
print(sum(sorted([int(x) for x in input().split()],reverse=1)[:k]))