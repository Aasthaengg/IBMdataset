
def main():

    numero = int(input())
    suma = 0
    for i in range(1, 4):

        suma = suma + numero**i

    print(suma)

if __name__ == "__main__":
    main()