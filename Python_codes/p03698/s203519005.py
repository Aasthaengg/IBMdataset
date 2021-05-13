

if __name__ == '__main__':
    s= input()
    len1 = len(s)
    len2 = len(set(s))

    if len1 == len2:
        print("yes")
    else:
        print("no")
