def main():
    line = input()
    mul = 1
    lista_lados = [int(x) for x in line.split()]
    index_max = lista_lados.index(max(lista_lados))
    for i in range(len(lista_lados)):
        if i != index_max:
            mul *= lista_lados[i]
    print(int(mul/2))
main()