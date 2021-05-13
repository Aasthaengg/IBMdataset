def main():
    o = list(input())
    e = list(input())
    s = []

    for i in range(len(o)+len(e)):
        if i % 2 == 0:
            s.append(o[i//2])
        else:
            s.append(e[i//2])
    
    print(''.join(s))

if __name__ == '__main__':
    main()