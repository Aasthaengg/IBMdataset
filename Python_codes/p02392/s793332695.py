class Range:
    def __init__(self, a, b, c):
        if a < b and b < c:
            print "Yes"
            return
        else:
            print "No"
            return

if __name__ == "__main__":
    a,b,c = map(int,raw_input().split())
    Range(a,b,c)