abc = list(map(int, input().split()))
abc.sort(reverse=1)
print(abc[0] * 10 + abc[1] + abc[2])
