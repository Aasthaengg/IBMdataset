N = int(input())
S = list(map(int, input().split(' ')))

if (len(S) - len(set(S))) % 2 == 0:
    print(len(set(S)))
else:
    print(len(set(S))-1)