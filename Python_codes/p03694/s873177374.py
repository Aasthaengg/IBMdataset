N = input()
L = list(reversed(sorted(list(map(int,input().split())))))
print(L[0]-L[-1])