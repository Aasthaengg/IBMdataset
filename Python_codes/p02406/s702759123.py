def call(n):
    ret = ""
    for i in range(1, int(n)+1):
        if 0 == i % 3:
            ret += " " + str(i)
        elif -1 != str(i).find("3"):
            ret += " " + str(i)

    return ret

if __name__ == "__main__":
    n = input()
    ret = call(n)
    print (ret)
