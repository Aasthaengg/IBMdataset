cnt = 0
def show_list(a):
    for x in a:
        print x

def g_decide(n):
    g = []
    i = 1
    while True:
        tmp = (3**i-1)/2
        if tmp>=n:
            if len(g)==0:
                g.append(1)
            break
        g.append(tmp)
        i+=1
    return g

def insertion_sort(a,n,g):
    global cnt
    for i in xrange(g,n):
        v = a[i]
        j = i-g
        while j >=0 and a[j]>v:
            a[j+g] = a[j]
            j = j-g
            cnt+=1
        a[j+g] = v

def shell_sort(a,n):
    g = sorted(g_decide(n),reverse=True)
    m = len(g)
    print m
    print " ".join(map(str,g))
    for i in xrange(m):
        insertion_sort(a,n,g[i])
    print cnt
    show_list(a)

def main():
    n = input()
    a = []
    for i in xrange(n):
        a.append(input())
    shell_sort(a,n)

if __name__ == '__main__':
    main()