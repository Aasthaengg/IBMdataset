mult_pair = input()

indiv = mult_pair.split(" ")
indiv = list(map(int, indiv))
product = indiv[0] * indiv[1]
print(product)
