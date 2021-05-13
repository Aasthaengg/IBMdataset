def eucli(a, b):
    r = a % b
    if r != 0:
        return eucli(b, r)
    else:
        return b

if __name__=="__main__":
    x, y = map(int, input().split())
    print(eucli(x, y))