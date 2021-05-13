from collections import Counter

def main():
    h,w,m=map(int,input().split())
    hw=set([tuple(map(int,input().split())) for _ in range(m)])
    hs=Counter([i[0] for i in hw])
    ws=Counter([i[1] for i in hw])
    hh = [hs.most_common()[0]]
    for i in hs.items():
        if i[1] == hh[0][1]:
            hh.append(i)
    ww = [ws.most_common()[0]]
    for i in ws.items():
        if i[1] == ww[0][1]:
            ww.append(i)
    
    for i in hh:
        for j in ww:
            if (i[0], j[0]) not in hw:
                #print(hw, i[0],j[0])
                print(i[1] + j[1])
                return
    else:
        print(hh[0][1]+ww[0][1]-1)

if __name__ == "__main__":
    main()