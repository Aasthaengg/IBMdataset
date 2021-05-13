#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C&lang=jp
#??????
if __name__ == "__main__":
    n_line = int(input())
    input_list = [tuple(input().split()) for i in range(n_line)]
    l = set([])
    for c, s in input_list:
        if c == "insert":
            l.add(s)
        else:
            if s in l:
                print("yes")
            else:
                print("no")