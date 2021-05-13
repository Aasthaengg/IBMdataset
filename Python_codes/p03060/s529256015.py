input()
print(sum([max(int(v)-int(c),0) for v,c in zip(input().split(),input().split())]))