def main():
    s = int(input())
    i = 1
    l = [s]
    flag = 0
    while flag == 0:
        if s % 2 == 0:
            s = s // 2
        else:
            s = 3*s + 1
        i += 1
        if s in l:
            print(i)
            return
        else:
            l.append(s)
main()  