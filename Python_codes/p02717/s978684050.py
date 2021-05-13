def main():
    x,y,z = map(int,input().split())
    x,y = swap(x,y)
    x,z = swap(x,z)
    print(x,y,z)

def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b


if __name__ == "__main__":
    main() 
