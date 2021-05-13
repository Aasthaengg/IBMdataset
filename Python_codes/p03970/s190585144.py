s = input()
a = "CODEFESTIVAL2016"
ans = [i != j for i, j in zip(s, a)]
print(sum(ans))