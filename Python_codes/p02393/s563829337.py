class SortingThreeNumbers:
    def __init__(self, n):
        n.sort()
        print "%(a)d %(b)d %(c)d" % {'a':n[0],'b':n[1],'c':n[2]}
        return

if __name__ == "__main__":
    n = (map(int, raw_input().split()))
    SortingThreeNumbers(n)