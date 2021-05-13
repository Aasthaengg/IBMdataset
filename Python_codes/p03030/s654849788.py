def main():
    n = int(input())
    l = []
    d = {}
    for i in range(n):
        s,p = input().split()
        if s not in l:
            l.append(s)
            d[s] = []
        d[s].append([int(p), i+1])
    
    for i in sorted(l):
        for j in sorted(d[i], reverse=True):
            print(j[1])
main()  