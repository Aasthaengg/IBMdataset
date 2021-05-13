numeros = input()
numeros = numeros.split()
resultado = [0,0,0]
resultado[0] = int(numeros[0]) + int(numeros[1])
resultado[1] = int(numeros[0]) - int(numeros[1])
resultado[2] = int(numeros[0]) * int(numeros[1])
print(max(resultado))