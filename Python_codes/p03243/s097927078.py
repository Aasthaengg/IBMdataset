
url = "https://atcoder.jp//contests/abc111/tasks/abc111_b"

def main():
    s = input()
    for n in range(int(s), 1000):
        str_n = str(n)
        if len(str_n) == str_n.count(str_n[0]):
            print(n)
            exit()



if __name__ == '__main__':
    main()
