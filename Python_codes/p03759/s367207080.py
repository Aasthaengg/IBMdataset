def main14():
    buf = input("");
    bufs = buf.split();
    hai = [];
    for i in range(len(bufs)):
        hai.append(int(bufs[i]));
    if hai[1] - hai[0] == hai[2] - hai[1]:
        print("YES");
    else:
        print("NO");

if __name__ == '__main__':
    main14()