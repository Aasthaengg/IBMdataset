def time(s):
    h = s // 3600
    s = s - h * 3600

    m = s // 60
    s = s - m * 60
    return str(h), str(m), str(s)

def main():
    t = int(input())
    h, m, s = time(t)
    print('{}:{}:{}'.format(h,m,s))


main()
