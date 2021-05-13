if __name__ == '__main__':
    a = int(input())
    s = input()
    count =0
    max = 0
    for i in s:
        if i == "I":
            count +=1
        else:
            count -=1

        if max < count:
            max = count
    print(max)
