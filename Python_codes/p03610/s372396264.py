
if __name__ == '__main__':
    a = input()
    s =""

    for i in range(len(a)):
        if i %2 ==0:
            s +=a[i]
    print(s)