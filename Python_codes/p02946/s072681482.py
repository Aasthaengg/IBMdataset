K, X = map(int, input().split())
lst = [X + i for i in range(-K+1, K)]
lst = [str(j) for j in lst]
lst = " ".join(lst)
print(lst)