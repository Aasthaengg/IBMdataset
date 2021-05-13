def main():
    l = int(input())
    # l = a + b + c 
    # c = l - a - b
    # v = ab(l-a-b)
    # v = b(-a**2 + (l-b)a)
    # v = b(-(a-(l-b)/2)**2 + (l-b)/2)**2)
    # a = (l-b)/2のときv_max=b*(（l-b）/2)**2
    # v_max = b(b**2 - 2*l*b + l**2)/4
    # v_max = (b**3 - 2*l*b**2 + l**2*b)/4
    # v_max' = (3*b**2 - 4*l*b + l**2)/4
    # v_max' = (3*b-l) * (b-l) / 4
    # 0 > b > l/3の時 単調増加
    # l/2 > b > 1 の時単調減少  
    # b = l/3の時v_maxとなる
    # a = (l-l/3)/2 = l/3
    ans = (l/3) ** 3
    print(ans)
     
if __name__ == '__main__':
    main()
