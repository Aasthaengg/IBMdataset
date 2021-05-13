def getval():
    n = int(input())
    h = list(map(int,input().split()))
    return n,h 

def main(n,h):
    dp = [0,abs(h[1]-h[0])]
    for i in range(1,n-1):
        x = dp[-1]+abs(h[i+1]-h[i])
        y = dp[-2]+abs(h[i+1]-h[i-1])
        dp.append(min(x,y))
    print(dp[-1])
        
if __name__=="__main__":
    n,h = getval()
    main(n,h)
