if __name__ == "__main__":
    date = input().replace("　", " ").split(" ")
    if date[0] <= date[1]:
        print(date[0])
    else:
        print(int(date[0])-1)