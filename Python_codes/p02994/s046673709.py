def main():
    import numpy as np
    n, l = map(int,input().split())
    inlis = []
    taishou = 10 *10000
    flag = 0

    for i in range(l, l+n):
        if taishou > np.abs(i):
            taishou = np.abs(i)
            if i < 0:
                flag = 1
        inlis.append(i)
    if flag == 0:
        print(sum(inlis) - taishou)
    else:
        print(sum(inlis) + taishou)

    
        

    
if __name__ == "__main__":
    main()
