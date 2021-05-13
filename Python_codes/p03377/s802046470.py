linha = input()
gatos, animais, X = [int(n) for n in linha.split()]

if (X >= gatos and animais + gatos >= X):
    print("YES")
else:
    print("NO")

