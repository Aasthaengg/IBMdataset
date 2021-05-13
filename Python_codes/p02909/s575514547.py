import sys


# input = sys.stdin.readline

def main():
    S = input()
    we = ["Sunny","Cloudy","Rainy"]
    if S ==we[0]:
        print(we[1])
    elif S ==we[1]:
        print(we[2])
    else:
        print(we[0])



if __name__ == "__main__":
    main()