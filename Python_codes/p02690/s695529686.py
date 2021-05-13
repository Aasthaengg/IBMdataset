X = int(input())
# A>=0で考えられる
div_list = []
for a in range(1, int(X**0.5)+1):
    if X % a == 0:
        div_list.append((a, X//a))

#print(div_list)
for x, y in div_list:
    for a in range(int(X**0.5)+1):
        b = a - x
        #print(a, b)
        y_hat = a**4 + b*a**3 + b**2*a**2 + b**3*a + b**4
        #print(y_hat)
        if y_hat == y:
            print(a, b)
            exit()