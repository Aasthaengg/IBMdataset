def main():
    s = input()
    g = s.count('g')
    p = s.count('p')
    if (g + p) % 2 == 0:
        return g - (g + p)//2
    else:
        return g - (g + p + 1)//2
print(main())
