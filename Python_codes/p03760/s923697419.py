def main():
    O = input()
    E = input()
    pas = ''
    for i in range(len(E)):
        pas += O[i] + E[i]
    if len(O) > len(E):
        pas += O[-1]
    print(pas)

if __name__ == '__main__':
    main()