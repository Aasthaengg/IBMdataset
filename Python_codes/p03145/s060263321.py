triangulo = input()
lados = triangulo.split()
AB = lados[0]
BC = lados[1]
area = (int(AB) * int(BC))/2
print("%.0f" % area)