n = int(input())
aa = list(map(int, input().split()))
print(sum([a%2 for a in aa[::2]]))