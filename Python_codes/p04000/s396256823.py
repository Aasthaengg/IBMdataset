import sys
input = sys.stdin.readline

def main():
    h,w,n = map(int,input().split())
    dg = 10**10
    d = dict()

    def f(x,y):
        if 2 <= x <= h-1 and 2 <= y <= w-1:
            return True
        else:
            False

    for i in range(n):
        a,b = map(int,input().split())
        
        if f((a-1),b-1):
            if (a-1)*dg + b-1 in d:
                d[(a-1)*dg + b-1] += 1
            else:
                d[(a-1)*dg + b-1] = 1
        
        if f((a-1),b):
            if (a-1)*dg + b in d:
                d[(a-1)*dg + b] += 1
            else:
                d[(a-1)*dg + b] = 1
        
        if f((a-1),b+1):
            if (a-1)*dg + b+1 in d:
                d[(a-1)*dg + b+1] += 1
            else:
                d[(a-1)*dg + b+1] = 1

        if f((a),b-1):
            if (a)*dg + b-1 in d:
                d[(a)*dg + b-1] += 1
            else:
                d[(a)*dg + b-1] = 1
        
        if f(a,b):
            if a*dg + b in d:
                d[a*dg + b] += 1
            else:
                d[a*dg + b] = 1
        
        if f((a),b+1):
            if (a)*dg + b+1 in d:
                d[(a)*dg + b+1] += 1
            else:
                d[(a)*dg + b+1] = 1
        
        if f((a+1),b+1):
            if (a+1)*dg + b+1 in d:
                d[(a+1)*dg + b+1] += 1
            else:
                d[(a+1)*dg + b+1] = 1
        
        if f((a+1),b):
            if (a+1)*dg + b in d:
                d[(a+1)*dg + b] += 1
            else:
                d[(a+1)*dg + b] = 1
        
        if f((a+1),b-1):
            if (a+1)*dg + b-1 in d:
                d[(a+1)*dg + b-1] += 1
            else:
                d[(a+1)*dg + b-1] = 1
        
        
        
        
    res = [0]*10
 
    for e in d:
        res[d[e]] += 1
 
    res[0] = (h-2)*(w-2)-sum(res)
 
    for e in res:
        print(e)
 
if __name__ == "__main__":
    main()
