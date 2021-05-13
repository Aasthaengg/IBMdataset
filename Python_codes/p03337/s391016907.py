def main():
    line = input()
    A, B = [int(n) for n in line.split()]
    lista = [A + B, A - B, A * B]
    print(max(lista))
main()