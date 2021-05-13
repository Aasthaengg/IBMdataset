
if __name__ == '__main__':
    a = input()
    b = input()
    asort=''.join(sorted(a))
    bsort=''.join(sorted(b,reverse=True))

    if asort <bsort:
        print("Yes")
    else:
        print("No")
