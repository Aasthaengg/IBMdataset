if __name__ == "__main__":
    i = 0
    while True:
        v = map( int, raw_input().split())
        if v[0] == 0:
            if v[1] == 0:
                break
        i += 1
        if v[0] > v[1]:
            print "{0} {1}".format(v[1],v[0])
        else:
            print "{0} {1}".format(v[0],v[1])