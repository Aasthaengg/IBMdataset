def main():
    n = int(input())
    vlis = list(map(int, input().split()))
    vlis.sort()
    mae = vlis[0]
    for i in range(1, n):
        ato = vlis[i]
        heikin = (mae + ato) / 2
        mae = heikin
    print(heikin)
    
if __name__ == "__main__":
    main()
