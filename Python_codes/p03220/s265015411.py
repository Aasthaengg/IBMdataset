def main():
    n=int(input())
    t,a=map(int,input().split())
    h=map(int,input().split())
    temp=[t-x*0.006 for x in h]
    m = (-1, 10**3)
    for i,v in enumerate(temp):
        d = abs(a-v)
        if m[1] >= d:
            m = (i, d)
    print(m[0]+1)
        
if __name__ == "__main__":
    main()