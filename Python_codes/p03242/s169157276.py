

def main():
    n = input()
    result = []
    for i in n:
        if i == '1':
            result.append('9')
        elif i == '9':
            result.append('1')
        else:
            result.append(i)
    print(result[0] + result[1] + result[2])


if __name__ == "__main__":
    main()
