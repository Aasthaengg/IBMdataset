while True:
    count = 0
    h,w = map(int ,raw_input().split())
    if h == w == 0:
        break
    for j in range(h):
        str1 = ""
        if count == 0:
            for i in range(w):
                if i % 2 == 1:
                    str1 += "."
                else:
                    str1 += "#"
            print str1
            count = 1
        else:
            for i in range(w):
                if i % 2 == 1:
                    str1 += "#"
                else:
                    str1 += "."
            print str1
            count = 0
    print "\n",