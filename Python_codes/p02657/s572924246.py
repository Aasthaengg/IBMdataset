def multi(a,b):
    return a * b

if __name__ == "__main__":
    a,b = input().split(" ")
    a = int(a)
    b = int(b)
    print(multi(a,b))