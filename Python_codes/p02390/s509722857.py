if __name__ == '__main__':
    param_seconds = int(raw_input())

    h = param_seconds / 3600
    rest_seconds = param_seconds % 3600

    m = rest_seconds / 60
    rest_seconds %= 60

    print "%s:%s:%s" % (h, m, rest_seconds)