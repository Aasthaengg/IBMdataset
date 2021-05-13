linha = input()
pessoaA, pessoaB = [int(n) for n in linha.split()]
if pessoaA > 8 or pessoaB > 8:
    print(":(")
else:
    print("Yay!")
