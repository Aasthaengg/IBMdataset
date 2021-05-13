import math
def main():
    t = [int(t)for t in input().split()]
    x,a = t[0],t[1]
    
    print(0 if x<a else 10)


if __name__ == "__main__":
    main()