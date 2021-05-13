def main():
    X = int(input())
    Y = 2*int(X**(1/5))+1
    for A in range(-Y,Y):
        for B in range(-Y,Y):
            if A**5 - B**5==X:
                return A,B

if __name__ == "__main__":
    A,B=main()
    print("{} {}".format(A,B))