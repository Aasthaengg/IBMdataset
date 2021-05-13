def main():
    n = int(input())
    a = n - 1
    b = 1
    menor = soma_digitos(a) + soma_digitos(b)
    temp = 0
    for i in range(n-2):
        a -= 1
        b += 1
        temp = soma_digitos(a) + soma_digitos(b)
        if menor > temp:
            menor = temp
    print(menor)

def soma_digitos(n):
    soma = 0
    while n >= 1:
        soma += n%10
        n = n//10
    return soma
main()