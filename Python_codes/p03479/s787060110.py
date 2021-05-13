S = input().split(" ")
X = int(S[0])
Y = int(S[1])

def calculate(x,y):
    i = 0

    while x * (2 ** i) <=y:
        i = i + 1

    print(i)

calculate(X,Y)