
def main():
    R, G, B, N = map(int, input().split())
    ans = 0
    #anslist = []
    for r in range(3005):
        rtmp = R*r
        if rtmp > N:
            break
        for g in range(3005):
            gtmp = G*g
            if gtmp > N:
                break
            btmp = N - (rtmp + gtmp)
            if btmp < 0:
                continue
            ans += btmp%B==0
            #if btmp%B==0:
            #    b = btmp//B
            #    anslist.append((r,g,b))
    
    #print(anslist)
    print(ans)

if __name__ == "__main__":
    main()
