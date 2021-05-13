def get_max(aa):
    mi = None
    for i,v in aa.items():
        if mi is None or v > mv:
            mi = i
            mv = v
    return mi

def main():
    k,t=map(int,input().split())
    aa={i:v for i,v in enumerate(map(int,input().split()),1)}
    mi = None
    while len(aa) > 1:
        mi = get_max({i:v for i,v in aa.items() if i != mi})
        if aa[mi] > 1:
            aa[mi]-=1
        else:
            del aa[mi]
    print(list(aa.values())[0]-1)

main()