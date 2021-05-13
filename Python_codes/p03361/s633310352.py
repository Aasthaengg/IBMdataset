def main():
    h, w = map(int, input().split())
    campus = []
    
    for i in range(h):
        campus.append(input())
    
    for y in range(h):
        for x in range(w):
            if campus[y][x] == '.':
                continue
            
            flg = True
            
            for l, k in [1, 0], [0, 1], [-1, 0], [0, -1]:
                ad_y, ad_x = y + l, x + k
                
                if ad_y < 0 or h <= ad_y or ad_x < 0 or w <= ad_x:
                    continue
                
                if campus[ad_y][ad_x] == '#':
                    flg = False
            
            if flg:
                print('No')
                return
    
    print('Yes')
    
if __name__ == '__main__':
    main()