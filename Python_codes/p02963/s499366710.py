def main():
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    s = int(input())
    
    #三角形の面積を座標から求める公式を使う
    #x1=y1=0としたとき、abs(x2*y3-x3*y2)/2でsが求められる
    #x2=10**9,y2=1で固定し、10**9*y3-x3=sを満たすz3,y3を求める

    v = 10**9

    x = (v-s%v)%v
    y = (s+x)//v

    print(0,0,10**9,1,x,y)

if __name__=='__main__':
    main()