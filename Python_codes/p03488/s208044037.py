def main():
    S = input()
    X, Y = map(int, input().split())
    d = 0
    L = [[0], [0]]
    for s in S:
        if s == 'T':
            d = 1 - d
            if L[d][-1] != 0:
                L[d].append(0)
        else:
            L[d][-1] += 1
    xs, ys = set([L[0][0] if S[0] == 'F' else 0]), set([0])
    for i in L[0][1 if S[0] == 'F' else 0:]:
        xs = set(x + i for x in xs) | set(x - i for x in xs)
    for i in L[1]:
        ys = set(y + i for y in ys) | set(y - i for y in ys)
    return X in xs and Y in ys

print('Yes' if main() else 'No')
