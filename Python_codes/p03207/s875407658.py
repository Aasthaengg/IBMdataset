
if __name__ == '__main__':
    n = int (input())
    list = []
    for i in range(n):
        list.append(int(input()))
    list.sort(reverse=True)
    list[0]= list[0]//2

    print(sum(list))