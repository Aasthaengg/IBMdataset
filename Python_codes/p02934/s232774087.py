# B - Resistors in Parallel
def main():
    _ = int(input())
    a = list(map(int, input().split()))
    t = 0

    for i in a:
        t += 1/i
    print(1/t)
    

if __name__ ==  "__main__":
    main()