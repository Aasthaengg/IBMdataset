def main24():
    data = input().split()
    num = []
    for i in range(2):
        num.append(int(data[i]))
    if num[1] % num[0] == 0:
        print((num[0]+num[1]))
    else:
        print((num[1]-num[0]))

if __name__ == "__main__":
    main24()