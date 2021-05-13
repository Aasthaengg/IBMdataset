li = list(map(int, input().split()))
uni = list(set(li))
print(sum(uni)*2-sum(li))