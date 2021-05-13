S = input()
N = len(S)
print(sum(map(lambda x: x[0] != x[1], zip(S[:N//2], S[::-1]))))