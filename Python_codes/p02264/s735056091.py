class process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def main():
    n, q = map(int, raw_input().split())
    p = list()
    for i in range(n):
        name, time = raw_input().split()
        p.append(process(name, int(time)))

    s = 0
    while len(p) > 0:
        e = p.pop(0)
        if e.time - q <= 0:
            s += e.time
            print(e.name + " " + str(s))
        else:
            s += q
            e.time -= q
            p.append(e)

main()