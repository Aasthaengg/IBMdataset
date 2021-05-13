import fileinput as fi
def gcd_euler(a,b):
    if b == 0: return a
    u = a
    v = b
    r = u % v
    while True:
        if r == 0:return v
        u = v
        v = r
        r = u % v



if __name__ == "__main__":
    for line in fi.input():
        a,b = list(map(int,line.strip().split()))
        if a > b:gcd=gcd_euler(a,b)
        else:gcd=gcd_euler(b,a)
        print(gcd,int((a*b)/gcd))