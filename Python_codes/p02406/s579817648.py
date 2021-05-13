class StructuredProgramming:
    def call(self, n):
        s = ""
        i = 1
        while i <= n:
            x = i
            if x % 3 == 0:
                s += " %d" % (i)
            else:
                while x:
                    if x % 10 == 3:
                        s += " %d" % (i)
                        break
                    x /= 10
            i += 1
        print s

if __name__ == "__main__":
    sp = StructuredProgramming()
    n = int(raw_input())
    sp.call(n)