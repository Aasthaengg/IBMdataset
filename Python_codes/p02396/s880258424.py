class PrintTestCases:
    def __init__(self):
        self.i = 1

    def output(self, x):
        print "Case %d: %d" % (self.i, x)
        self.i += 1

if __name__ == "__main__":
    ptc = PrintTestCases();
    while True:
        x = int(raw_input())
        if x == 0:
            break
        ptc.output(x)