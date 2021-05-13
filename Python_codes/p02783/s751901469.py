H, A = map(int, input().split())

X = H//A

print(X if H%A == 0 else X+1)
